from django import forms


class TestForm(forms.Form):
    textarea = forms.CharField(max_length=500, widget=forms.Textarea, required=True, strip=False)
    remove_punctuations = forms.BooleanField(required=False)
    upper_case = forms.BooleanField(required=False)
    lower_case = forms.BooleanField(required=False)
    new_line_remove = forms.BooleanField(required=False)
    extra_space_remove = forms.BooleanField(required=False)
    count_characters = forms.BooleanField(required=False)
    spell_check = forms.BooleanField(required=False)
    generate_word_summary = forms.BooleanField(required=False)
    remove_stop_words = forms.BooleanField(required=False)
