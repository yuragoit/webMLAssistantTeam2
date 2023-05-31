from django.template.defaulttags import url
from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    # The home page
    path("", views.upload, name="upload"),
    path("archives/", views.archives, name="archives"),
    path("images/", views.images, name="images"),
    path("video/", views.video, name="video"),
    path("documents/", views.documents, name="documents"),
    path("programs/", views.programs, name="programs"),
    path("audio/", views.audio, name="audio"),
    path('download/<str:name>', views.download, name="download"),
    path('downloads/', views.render_downloads_page, name="downloads"),
    path("others/", views.others, name="others"),
    path("delete/<str:name>", views.delete_file, name="delete"),
]
