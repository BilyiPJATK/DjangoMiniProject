from django import forms

from my_app.models import ContactFormSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['email', 'message']