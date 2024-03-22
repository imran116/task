from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from chatApp.forms import CreateUser, Q_form
from django.contrib.auth import login, logout, authenticate

# hugchat
from hugchat import hugchat
from hugchat.login import Login


# Create your views here.
@login_required
def index_view(request):
    return render(request, 'index.html')


def register_view(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'authentication/signup.html', context={'form': form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'authentication/login.html', context={'form': form})


def get_recipe(request):
    if request.method == 'POST':
        form = Q_form(data=request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            # Log in to huggingface and grant authorization to huggingchat
            sign = Login("imranhossain", "i(iUEge!)YQ;g7^")
            cookies = sign.login()
            cookie_path_dir = "./cookies_snapshot"
            sign.saveCookiesToDir(cookie_path_dir)
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            id = chatbot.new_conversation()
            chatbot.change_conversation(id)
            msg = query
            response = chatbot.chat(msg)
            model_obj = form.save(commit=False)
            model_obj.query = msg
            model_obj.ai_response = response
            form.save()
            return render(request, 'index.html', context={'msg': msg, 'response': response, })
        else:
            error = form.errors
            print(error)
            return render(request, 'index.html', context={'error': error})

    return redirect('home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
