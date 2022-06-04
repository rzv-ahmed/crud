from django import forms

from . import models
class stu_reg(forms.ModelForm):
    class Meta:
        model=models.stu_form
        fields="__all__"
