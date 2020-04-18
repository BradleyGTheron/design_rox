from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm, EditProfileForm, ChangePasswordForm

# LOGS IN A USER
def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Login Error - Please Try Again!'))
            return redirect('auth:login')
    else:
        return render(request, 'authenticate/login.html', {})

# LOGS OUT A USER
def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out!'))
    return redirect('home')

# REGISTER A NEW USER
def register_user(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered'))
            return redirect('home')
    else:
        form = RegistrationForm()

    context = {'form':form }
    return render(request, 'authenticate/register.html', context)

# EDIT A USERS PROFILE

def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, ('You Have Edited Your Profile !'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {'form': form, 'profile_form':profile_form }
    return render(request, 'authenticate/edit_profile.html', context)

# CHANGES THE USERS change_passowrd

def change_password(request):
    if request.method=='POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You Have Edited Your Profile !'))
            redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)

    context = {'form' : form}
    return render(request, 'authenticate/change_password.html', context)
