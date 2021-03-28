from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    context = {}
    return render (request, 'index.html', context)

def event_page_view(request):
    context = {}
    return render(request, 'event_page.html', context)

def search_event_page(request):
    context = {'f'}
    return render(request, 'search_event_page.html', context)

def my_events_page_view(request):
    context = {}
    return render(request, 'my_events_page.html', context)

def create_event_page_view(request):
    context = {}
    return render (request, 'create_event_page.html', context)

def edit_event_page_view(request):
    context = {}
    return render (request, 'edit_event_page.html', context)

def login_signup_page_view(request):
    context = {}
    return render(request, 'login_signup_page.html', context)

def forgot_password_page_view(request):
    context = {}
    return render(request, 'forgot_password.html', context)

