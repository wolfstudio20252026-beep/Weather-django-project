from django import forms

class CitySearchForm(forms.Form):
    city = forms.CharField(
        label='Город',
        max_length=100
    )