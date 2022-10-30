from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Home Page'

        return context


class IndexPage(TemplateView):
    template_name = 'index.html'
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_name'] = 'Smart App'

        return context
