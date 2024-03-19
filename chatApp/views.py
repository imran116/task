import json
from django.contrib.auth.decorators import login_required
from chatApp.models import Recipe
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from chatApp.forms import CreateUser, Q_form
from django.contrib.auth import login, logout, authenticate
import requests


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
    api_key = "9pUgmOV/FJg/tVFzfEyV9w==NmpTRVsskmtliRIf"
    form = Q_form()
    if request.method == 'POST':
        form = Q_form(data=request.POST)
        if form.is_valid():

            query = form.cleaned_data.get('query')
            api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
            response = requests.get(api_url, headers={'X-Api-Key': api_key})
            if response.status_code == requests.codes.ok:
                recipe = json.loads(response.text)
                for item in recipe:
                    title = item['title']
                    ingredients = item['ingredients']
                    servings = item['servings']
                    instructions = item['instructions']
                    form_obj = form.save(commit=False)
                    form_obj.title = title
                    form_obj.ingredients = ingredients
                    form_obj.instructions = instructions
                    form_obj.servings = servings
                    form.save()
                    return render(request, 'index.html', context={
                        'title': title,
                        'ingredients': ingredients,
                        'servings': servings,
                        'instructions': instructions})
            else:
                print("Error:", response.status_code, response.text)

            print(query)
    return redirect('home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
