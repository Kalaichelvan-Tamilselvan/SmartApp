from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import TestForm
from .logic import (punctuation_removal,
                    text_upper,
                    text_lower,
                    remove_newline,
                    extra_space_remove,
                    count_characters,
                    text_spellchecker,
                    summary_generate,
                    remove_stopwords,
                    )


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
        changed_data['Your sentence with Removed Punctuations'] = punctuation_removal(text)
        current_text = punctuation_removal(current_text)

    if bool(form_data['upper_case']):
        changed_data['Your Upper Case text'] = text_upper(current_text)
        current_text = text_upper(current_text)

    if bool(form_data['lower_case']):
        changed_data['Your Lower Case text'] = text_lower(current_text)
        current_text = text_lower(current_text)

    if bool(form_data['new_line_remove']):
        changed_data['Your sentence with New Line Removed'] = remove_newline(current_text)
        current_text = remove_newline(current_text)

    if bool(form_data['extra_space_remove']):
        changed_data['Your sentence with Extra Space Removed'] = extra_space_remove(current_text)
        current_text = extra_space_remove(current_text)

    if bool(form_data['count_characters']):
        changed_data['Your total Count of Characters'] = count_characters(current_text)

    if bool(form_data['spell_check']):
        changed_data['Your Spell Check for the text is'] = text_spellchecker(current_text)
        current_text = text_spellchecker(current_text)

    if bool(form_data['generate_word_summary']):
        changed_data['Your summary for the word is'] = summary_generate(current_text)
        current_text = summary_generate(current_text)

    if bool(form_data['remove_stop_words']):
        changed_data["Your sentence with Removed Stop Words"] = remove_stopwords(current_text)
        current_text = remove_stopwords(current_text)

    context = {
        'current_text': current_text,
        'content': changed_data
    }
    return render(request, template_name='guide.html', context=context)
