from django import forms



class CompanyForm(forms.Form):
    company_name = forms.CharField(max_length=50)


class CompanyGetForm(forms.Form):
    company_name = forms.CharField(max_length=50, required=True)