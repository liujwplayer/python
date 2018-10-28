from django import forms


class ParkForm(forms.Form):
    company_id = forms.CharField(required=False)
    park_name = forms.CharField()