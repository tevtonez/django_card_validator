"""Views."""

from django.http import JsonResponse

from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms import CardValidatorForm


class IndexView(FormView):
    """Main view."""

    template_name = 'index.html'
    form_class = CardValidatorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        """Get context data."""
        print("processing get")
        context = super(IndexView, self).get_context_data(**kwargs)
        print(context)
        return context


def checksum(request):
    """Endpoint to check the card number."""
    result = 'Entered card number is Invalid!'
    result_class = 'danger'
    card_number = str(request.GET.get('card_number', None))

    if len(card_number) > 0:
        sum = 0
        num_digits = len(card_number)
        oddeven = num_digits & 1

        for count in range(0, num_digits):
            digit = int(card_number[count])

            if not ((count & 1) ^ oddeven):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9

            sum = sum + digit

        if (sum % 10) == 0:
            result = 'Your card number is Valid.'
            result_class = 'success'

    else:
        result = 'Please enter card number.'

    data = {
        'result': result,
        'result_class': result_class
    }
    return JsonResponse(data)
