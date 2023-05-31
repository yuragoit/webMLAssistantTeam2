from django import forms
from .models import Note, Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "some short description",
            }
        ),
    )

    class Meta:
        model = Tag
        fields = ["name"]


class NoteForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "some short description with #Key_word",
            }
        )
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "full description",
            }
        )
    )

    class Meta:
        model = Note
        fields = ["name", "description", "done"]
        exclude = ["tags"]
