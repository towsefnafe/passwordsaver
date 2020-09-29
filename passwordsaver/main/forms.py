from django import forms

class CreateNewList(forms.Form):
	website = forms.CharField(label="Website", max_length=300)
	username = forms.CharField(label="Username", max_length=300)
	password = forms.CharField(label="Password", max_length=300)
