from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from main.forms import CardValidatorForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = CardValidatorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        print("processing get")
        context = super(IndexView, self).get_context_data(**kwargs)
        print(context)
        return context


def checksum(request):

    form = CardValidatorForm(request.POST)

    print(form)

    result = 'NOT VALID!'

    if request.method == "POST":
        print(request.POST)

        card_number = str(form.cleaned_data['card_number'])
        # card_number = '4874120048361894'

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
            result = 'VALID!'

    data = {'result': result}
    return JsonResponse(data)
