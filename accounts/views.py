from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm, SignUpForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import Poll
from .models import Profile

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
            messages.error(request, 'username or password is incorrect')
            
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'accounts/sign-in.html')        

def sign_up(request):    
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_account = form.save()
            Profile.objects.create(user=user_account)            
            messages.success(request, 'Sign up successfully')
            return redirect('sign-in')

    context = {'form': form}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'accounts/sign-up.html', context)

def profile(request):    
    user_profile = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    user_form = UserUpdateForm(instance=request.user)
    profile_image_url = user_profile.profile_picture.url
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been updated!')
            return redirect('profile')
    
    context = {'profile_form': profile_form, 'user_form': user_form, 'profile_image_url': profile_image_url}
    return render(request, 'accounts/profile.html', context)

@login_required
def creator_profile(request, profile_slug, profile_uuid):
    user_profile = Profile.objects.get(profile_uuid=profile_uuid)
    profile_image_url = user_profile.profile_picture.url
    
    context = {'user_profile': user_profile, 'profile_image_url': profile_image_url}
    return render(request, 'accounts/creator-profile.html', context)

def sign_out(request):
    logout(request)
    return redirect('sign-in')