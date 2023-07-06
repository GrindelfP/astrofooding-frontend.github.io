from django import forms


class DietaryForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0)
    weight = forms.FloatField(min_value=0)
    height = forms.FloatField(min_value=0)
    gender = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')))
