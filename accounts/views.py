from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def sign_in(request):
    valuenext = request.POST.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if valuenext != '':
                return redirect(valuenext)
            else:
                return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'accounts/sign-in.html')        

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign up successfully')
            return redirect('sign-in')

    context = {'form': form}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'accounts/sign-up.html', context)

def sign_out(request):
    logout(request)
    return redirect('sign-in')