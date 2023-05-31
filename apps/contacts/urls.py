from django.urls import path
from .views import ContactsListView, ContactCreateView, ContactUpdateView, ContactDeleteView

app_name = 'contacts'

urlpatterns = [
    path('', ContactsListView.as_view(), name='contact_list'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_delete'),
    path('update/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
]
