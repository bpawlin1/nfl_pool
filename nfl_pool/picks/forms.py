# forms.py
from django import forms
from .models import Pick

class PickForm(forms.ModelForm):
    class Meta:
        model = Pick
        fields = ['team', 'week']