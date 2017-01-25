import re
from django import forms
class NameForm(forms.Form):
    weight = forms.IntegerField(label='weight')
    height = forms.IntegerField(label='height')
    length = forms.IntegerField(label='width')
    width = forms.IntegerField(label='length')
    user = forms.CharField(label='Your Name', max_length=100)
    location_from=forms.CharField(label='location from', max_length=30) 
    location_to=forms.CharField(label='location to', max_length=30) 