from django import forms

from view_app import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'
