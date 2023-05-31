from django.urls import path
from .views import NotesListView, NotesDeleteView, note, set_done, detail, note_update

app_name = "notes"

urlpatterns = [
    path("", NotesListView.as_view(), name="notes_list"),
    path("create/", note, name="note_create"),
    path("done/<int:pk>", set_done, name="notes_set_done"),
    path("detail/<int:pk>/", detail, name="note_detail"),
    path("update/<int:pk>/", note_update, name="note_update"),
    path("delete/<int:pk>/", NotesDeleteView.as_view(), name="note_delete"),
]
