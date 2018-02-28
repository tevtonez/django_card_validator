"""Views."""

from django.http import JsonResponse

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_exempt

from main.forms import CardValidatorForm

import unicodedata


class IndexView(FormView):
    """Main view."""

    template_name = 'index.html'
    form_class = CardValidatorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


@csrf_exempt
def checksum(request):
    """Endpoint to check the card number."""
    result = 'Entered card number is Invalid!'
    result_class = 'danger'

    if request.method == 'POST':

        card_number = str(request.POST.get('card_number', None))
        is_number = False

        try:
            float(card_number)
            is_number = True
        except ValueError:
            pass

        try:
            unicodedata.numeric(card_number)
            is_number = True
        except (TypeError, ValueError):
            pass

        if len(card_number) > 0:

            if is_number:
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
                result = 'Please enter digits only.'

        else:
            result = 'Please enter a card number.'

        data = {
            'result': result,
            'result_class': result_class
        }
    return JsonResponse(data)
