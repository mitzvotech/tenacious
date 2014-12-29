from django import forms
from app.models import Client, Matter, Document, Bundle

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['id']

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        exclude = ['id']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['id']

class BundleForm(forms.ModelForm):
    class Meta:
        model = Bundle
        exclude = ['id']
