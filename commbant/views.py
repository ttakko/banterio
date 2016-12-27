from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import mail_managers
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages import get_messages
from django.views.decorators.csrf import *
from django.core import mail
from datetime import datetime
import json
from .forms import *
from .models import *

@login_required(login_url='/login/')
def logout(request):
    logout_user(request)
    return HttpResponseRedirect("/")


def register(request):
    """
    Handles registering user
    form(template): Registering form
    """
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'],
                                            first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'], password = form.cleaned_data['password1'])
            #userobj = User.objects.get(username=user.username)
            #sprof, created= MyUser.objects.get_or_create(user=userobj)
            user.save()
            return HttpResponseRedirect("/login/")

    return render_to_response("register.html",
                    {"form":form},
                    context_instance=RequestContext(request))

def login(request):
    """
    This view handles user authentication
    """

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    form = AuthenticationForm()

    if username != "":
        user = authenticate(username=username, password=password)
        if user is not None:
            user1 = User.objects.get(username = user.username)
            if MyUser.objects.all().filter(user = user1):
                myuser = MyUser.objects.get(user=user1)
                login_user(request, user)
                return HttpResponseRedirect("/")
            else: return HttpResponse("U don goofd boi")
        else: form = AuthenticationForm(initial={"username":username})
    #form.fields['password'].widget.attrs['autofocus'] = 'on'
    return render(request, "login.html", {"form":form})

@login_required(login_url='/login/')
def create_group(request):
        form = GroupCreationForm()
        if request.method == "POST":
            form = GroupCreationForm(request.POST)
            if form.is_valid():
                group = Group.objects.create(name = form.cleaned_data['Name'], moderator = request.user)
                group.save()
                return HttpResponseRedirect("/")
        return render_to_response("register.html",
                        {"form":form},
                        context_instance=RequestContext(request))

#This is the main function gathering the chat
@csrf_exempt
@login_required(login_url='/login/')
def chat(request, group_cur):
    blog = Msg.objects.all().filter(group = group_cur)
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            massag = Msg.objects.create(user = form.cleaned_data['user'], content = form.cleaned_data['content'])
            massag.save()
            return HttpResponseRedirect('/chat/')
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'blog': blog, 'form':form})
