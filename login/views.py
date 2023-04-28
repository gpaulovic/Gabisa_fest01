from django.shortcuts import redirect, render
from .forms import CustomAuthForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm

def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
    
class IndexView(TemplateView):
    template_name = 'index.html'
    

class LogoutView(LogoutView):
    next_page = 'login'
