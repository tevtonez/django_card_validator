"""main app forms."""
from django import forms


class CardValidatorForm(forms.Form):
    """A single field that is used to get a card num from a user."""

    card_number = forms.IntegerField(label="Enter card number ")
