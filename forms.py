from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
