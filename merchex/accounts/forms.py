from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class MyLoginForm(AuthenticationForm):
   password = forms.CharField(widget=forms.PasswordInput(render_value=False))



class MyRegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname','email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(MyRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']

        if commit:
            user.save()
        return user

