#coding:utf-8

# Create your views here.
from .models import Message
from django.http import HttpResponse
from django.shortcuts import render,redirect
from forms import MessageForm

def hello(request):
    return HttpResponse("Hello message")	


# def message_message_list(request,template_name='message_list.html'):
#     """
#     Returns a news detail page.
#     """
#     message_list = Message.objects.all()
#     return render(request, template_name, {
#         'message_list': message_list,
#     })


def message_create(request, template_name='contact.htm'):
    message_list = Message.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = MessageForm()
    return render(request, template_name, {
        'form': form,
        'message_list': message_list,
    })
