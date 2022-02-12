from django.forms import ModelForm
from django import forms

from app.models import TODO


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your search: ")
