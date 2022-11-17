from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from smartapplication.forms import TestForm


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Welcome'

        return context


class IndexPage(FormView):
    template_name = 'index.html'
    form_class = TestForm
    success_url = reverse_lazy('Guide')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class GuidePage(TemplateView):
    template_name = 'guide.html'
    context_object_name = 'guide'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
