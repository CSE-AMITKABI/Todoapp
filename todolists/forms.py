from django import forms
class TodolistForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter todo eg. go to shopping','aria-lable':'todo','aria-describeby':'add-btn'})
    )
