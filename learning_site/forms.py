from django import forms
from django.core import validators


# Custom validator
def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Please verify your email')
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label='Leave empty',
                               validators=[must_be_empty, ])  # validators.MaxLengthValidator(0)

    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError("Unable to Save.")
    #     return honeypot

    def clean(self):
        """Do not requred to return cleaned data line clean_honeypot"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')
        if email != verify:
            raise forms.ValidationError("Please enter same email")
