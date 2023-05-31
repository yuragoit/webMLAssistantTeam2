import re
from .models import Note, Tag
from .forms import NoteForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from apps.common.mixins import TitleMixin


# Create your views here.
class NotesListView(TitleMixin, ListView):
    title = "Notes"
    template_name = "notes/app_notes.html"
    model = Note

    def get_queryset(self):
        queryset = super().get_queryset()
        notes = queryset.filter(user=self.request.user)
        for note in notes:
            note.teg_list = ", ".join([str(name) for name in note.tags.all()])

        return notes


# class NotesCreateView(TitleMixin, SuccessMessageMixin, CreateView):
#    title = "Create note"
#    template_name = "notes/note_add.html"
#    form_class = NoteForm
#    success_url = reverse_lazy("notes:notes_list")
#
#
#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super().form_valid(form)


@login_required
def note(request):
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            key_words_in_name = re.findall(r"#(\w+)", note.name)
            note.name = note.name.strip().replace("#", "").replace("_", " ")
            note.user = request.user
            note.save()
            tags_names = request.POST.getlist("tags")
            tags_names.extend(key_words_in_name)
            for tag_name in tags_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name, user=request.user)
                note.tags.add(tag)

            return redirect(to="notes:notes_list")
        else:
            return render(
                request,
                "notes/note_add.html",
                context={"form": form, "title": "Create note", "tags": tags},
            )

    return render(
        request,
        "notes/note_add.html",
        context={"form": NoteForm(), "title": "Create note", "tags": tags},
    )


@login_required
def note_update(request, pk):
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = get_object_or_404(Note, pk=pk, user=request.user)

            key_words_in_name = re.findall(r"#(\w+)", request.POST.get("name"))
            note.name = (
                request.POST.get("name").strip().replace("#", "").replace("_", " ")
            )
            note.description = request.POST.get("description")
            note.done = bool(request.POST.get("done", False))

            tags_names = request.POST.getlist("tags")
            tags_names.extend(key_words_in_name)
            note.tags.clear()
            for tag_name in tags_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name, user=request.user)
                note.tags.add(tag)

            note.save()

            return redirect(to="notes:notes_list")
        else:
            return render(
                request,
                "notes/note_update.html",
                context={"form": form, "title": "Update note", "tags": tags},
            )

    note = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(instance=note)
    form.data["note_tags"] = note.tags.all()

    return render(
        request,
        "notes/note_update.html",
        context={"form": form, "title": "Update note", "tags": tags},
    )


@login_required
def set_done(request, pk):
    Note.objects.filter(pk=pk, user=request.user).update(done=True)
    return redirect(to="notes:notes_list")


@login_required
def detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.teg_list = ", ".join([str(name) for name in note.tags.all()])
    return render(
        request,
        "notes/note_detail.html",
        context={"note": note, "title": "Note detail"},
    )


class NotesDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("notes:notes_list")
