from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import TestForm
from .logic import punctuation_removal, text_upper


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

    def form_valid(self, form):
        global form_data
        form_data = form.cleaned_data
        return super().form_valid(form)


def GuidePage(request):
    changed_data = {}
    text = form_data['textarea']
    current_text = text
    if bool(form_data['remove_punctuations']):
        changed_data['Remove Punctuations:'] = punctuation_removal(text)
        current_text = punctuation_removal(current_text)
    if bool(form_data['upper_case']):
        changed_data['Upper Case:'] = text_upper(current_text)
        current_text = text_upper(current_text)
    context = {
        'current_text': current_text,
        'content': changed_data
    }
    return render(request, template_name='guide.html', context=context)