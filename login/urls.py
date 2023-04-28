from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm
from .views import IndexView, LogoutView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name='login'),
    path('', IndexView.as_view(), name= 'index'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
