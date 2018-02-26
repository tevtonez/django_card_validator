from django import forms


class CardValidatorForm(forms.Form):
    card_number = forms.IntegerField(label="Enter card number ")
