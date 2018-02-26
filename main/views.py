from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from . import forms
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


# class mainIndexView(TemplateView):
#     template_name = 'main/base.html'
