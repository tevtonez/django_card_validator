from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
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
        return context

    def form_valid(self, form):
        print(form.cleaned_data['card_number'])
        return super(IndexView, self).form_valid(form)
