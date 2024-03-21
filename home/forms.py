# forms.py
from django import forms

class MemberSearchForm(forms.Form):
    query = forms.CharField(label='Search')
