import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from chat.forms import SignUpForm
from chat.models import User


def chat(request):
    users_list = User.objects.all()

    context = {
        'users_list': users_list
    }

    return render(request, 'chat/chat.html', context)


def index(request):
    user_list = User.objects.all()

    context = {
        'title': 'ListUser',
        "users_list": user_list
    }
    return render(request, 'chat/index.html', context)


@login_required
def room(request, room_name):
    user_list = User.objects.all()
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        "users_list": user_list
    }

    return render(request, 'chat/room.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            # user_group = Group.objects.get(name='User')
            # user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.status == 'b':
                    return redirect('block')
                return redirect('webchat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})


def signout_veiw(request):
    logout(request)
    return redirect('login')
