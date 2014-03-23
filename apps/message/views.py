#coding:utf-8

# Create your views here.
from .models import Message
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
#from forms import MessageForm

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
    #message_list = Message.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        telephone = request.POST.get('telephone', None)
        content = request.POST.get('message', None)
        try:
            Message.objects.create(name=name,email=email,tel=telephone,content=content)
            #response = 'success'
        except:
            pass
            #response = 'error'
        return redirect("/contact")
    return render_to_response(template_name)
