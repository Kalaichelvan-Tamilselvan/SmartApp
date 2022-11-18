from django import forms


class TestForm(forms.Form):
    textarea = forms.CharField(max_length=500, widget=forms.Textarea, required=True)
    RemovePunctuations = forms.BooleanField(required=False)
    UpperCase = forms.BooleanField(required=False)
    LowerCase = forms.BooleanField(required=False)
    NewLineRemove = forms.BooleanField(required=False)
    ExtraSpaceRemove = forms.BooleanField(required=False)
    CountCharacters = forms.BooleanField(required=False)
    SpellCheck = forms.BooleanField(required=False)
    GenerateSummary = forms.BooleanField(required=False)
    RemoveStopWords = forms.BooleanField(required=False)

