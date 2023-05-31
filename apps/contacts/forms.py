from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Bob',
    }))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+380661234567',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@gmail.com',
    }), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'UA, Kiev, Some Street 0',
    }), required=False)
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }), required=False)

    class Meta:
        model = Contact
        fields = ['first_name', 'phone_number', 'email', 'birthday', 'address']