from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(label='ФИО', max_length=100)
    email = forms.EmailField(required=True)
    agreement = forms.BooleanField(required=True, label='Согласие на обработку персональных данных')

    class Meta:
        model = User
        fields = ("full_name", "username", "email", "password1", "password2", "agreement")
