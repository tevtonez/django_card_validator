from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class CardValidatorForm(forms.Form):
    card_number = forms.IntegerField(
        label="Enter card number ",
        widget=forms.TextInput(attrs={'size': '22'})
    )
