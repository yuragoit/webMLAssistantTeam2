import operator
from functools import reduce
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Now
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import timedelta, datetime

from apps.common.mixins import TitleMixin
from .models import Contact, AddressBook
from .forms import ContactForm


class ContactsListView(TitleMixin, ListView):
    title = 'Contacts'
    template_name = 'contacts/contacts.html'
    model = Contact

    def get_queryset(self):
        try:
            book = AddressBook.objects.get(user=self.request.user)
        except:
            return None

        queryset = super().get_queryset()
        queryset = queryset.filter(address_book=book)
        if self.request.POST.get('birthday_option'):
            in_days = int(self.request.POST.get('birthday_option'))
            # Build the list of month/day tuples
            dates = []
            from_date = datetime.now().date()
            to_date = datetime.now().date() + timedelta(in_days)

            while from_date <= to_date:
                dates.append((from_date.month, from_date.day))
                from_date += timedelta(days=1)

            # Transform each into queryset keyword args
            dates = (dict(
                zip(('birthday__month', 'birthday__day'), t)) for t in dates)
            queryset_prepare = reduce(operator.or_, (Q(**d) for d in dates))
            queryset = queryset.filter(queryset_prepare)

        elif self.request.POST.get('birthday_option_in'):
            in_days = int(self.request.POST.get('birthday_option_in')) - 1
            print(in_days)
            queryset = queryset.filter(birthday__gte=Now() + timedelta(days=in_days))

        return queryset

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContactCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'Create contact'
    template_name = 'contacts/contact_add.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact_list')

    def form_valid(self, form):
        book, _ = AddressBook.objects.get_or_create(user=self.request.user)
        form.instance.address_book = book
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:contact_list')


class ContactUpdateView(TitleMixin, UpdateView):
    title = 'Update Contact'
    template_name = 'contacts/contact_update.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact_list')

