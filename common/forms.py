"""
created at: 2023-03-04
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    """
    user
    """
    email = forms.EmailField(label="이메일")

    class Meta:
        """
        form for sign up
        """
        model = User
        fields = ("username", "password1", "password2", "email")
