from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
from .forms import UserProfileForm, UserLoginForm


def signup_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Yep works</h1>')
        else:
            return HttpResponse('<h1>Something went wrong</h1>')
    
    else:
        # create blank form instance and displaying it
        form = UserProfileForm()
        context = {'form':form}
        return render(request, 'registration/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST )
        if form.is_valid():
            form.save()
            #return HttpResponse('<h1>Yep works</h1>')
        else:
            return HttpResponse('<h1>Yep Error</h1>')
    else:
        form = AuthenticationForm()
        context={'form':form}
        return render(request, 'registration/login.html', context)


def forgot_password_page_view(request):
    context = {}
    return render(request, 'forgot_password.html', context)

def session_manipulating_page(request):
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1
    
    #user = User.objects.create_user('ferean', 'feran@sdacademy.dev', 'password') 
    
    context = {
        'visit_count': visit_count,
    }
    
    return render(request, 'login_signup_page.html', context=context)
