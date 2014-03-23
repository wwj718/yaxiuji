#coding=utf-8

from django import forms

from .models import Message
 

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['response']
    


