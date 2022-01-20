from logging import PlaceHolder
from django import forms

class BasicForm(forms.Form):
    firstname=forms.CharField(max_length=10,widget=forms.widgets.TextInput(attrs={
        "placeholder":"First Name",
        "class":"form-control",
    }))
    lastname=forms.CharField(max_length=10,widget=forms.widgets.TextInput(attrs={
        "placeholder":"Last Name",
        "class":"form-control",
    }))
    gender=forms.ChoiceField(choices=((1,'Male'),(2,'Female')),widget=forms.Select(attrs={
        "class":"form-select"
    }))
    email_adress=forms.EmailField(widget=forms.widgets.EmailInput(attrs={
        "placeholder":"Enter email",
        "class":"form-control",
    }))
    phone_number=forms.CharField(max_length=11,widget=forms.widgets.NumberInput(
        attrs={
            "placeholder":"Enter mobile number",
            "class":"form-control",
        }
    ))




