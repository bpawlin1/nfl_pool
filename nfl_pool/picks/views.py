
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Team
from .forms import PickForm

def index(request):
    # Add any context data you want to pass to the template
    return render(request, 'index.html')

@login_required
def make_pick(request):
    if request.method == 'POST':
        form = PickForm(request.POST)
        if form.is_valid():
            # Handle pick creation and saving the form data
            pick = form.save(commit=False)
            pick.user = request.user  # Assign the currently logged-in user to the pick
            pick.save()
            return redirect('pick_success')  # Redirect to a success page or another appropriate view
    else:
        form = PickForm()

    return render(request, 'make_pick.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL where users should be redirected after registration.
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})