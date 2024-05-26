from django import forms

from taskman.models import home
from taskman.models import Task
from taskman.models import Chat

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
   first_name = forms.CharField()
   last_name = forms.CharField()
   email = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput())
   class Meta:
       model = User
       fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class TaskForm(forms.ModelForm):
   #content = forms.CharField(max_length=500, required=True)
   #difficulty = forms.ChoiceField(choices=Task.DIFFICULTY_CHOICES)
   #progress = forms.ChoiceField(choices=Task.PROGRESS_CHOICES)
   #comment = forms.CharField(max_length=1000, required=True)
   class Meta:
      model = Task
      exclude = ('active', 'user',)



class ChatForm(forms.ModelForm):
   class Meta:
      model = Chat
      exclude = ('active', 'user',)




