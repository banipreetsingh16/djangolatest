from django import forms
from myapp.models import DataBase

# class RegisterForms(forms.Form):
#     num1 = forms.CharField()
#     num2 = forms.CharField()

class DataBaseForm(forms.ModelForm):
    class Meta:
        model = DataBase
        fields = ['first_name','middle_name','last_name','work_experience','latest_education_degree','is_published']

