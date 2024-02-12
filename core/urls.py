from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .form import LoginForm


app_name = 'core'
urlpatterns = [
    path('about/', views.about ,name="store-about"),
    path('contact/', views.contact ,name="store-contact"),
    path('privacy_and_policy/', views.privacy_and_policy ,name="store-privacy_and_policy"),
    path('term_of_use/', views.term_of_use ,name="store-term_of_use"),
    path('signup/', views.signup ,name="store-singup"),
    path('',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name="store-login"),
    path('index/',views.index,name="store-index"),
]
