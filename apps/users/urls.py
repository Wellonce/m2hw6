from django.urls import path

from .views import UserLoginView, UserRegisterView, HomeView

urlpatterns = [
    path('', HomeView.as_view() , name="home-page"),
    path('register/', UserRegisterView.as_view() , name="register-page"),
    path('login/', UserLoginView.as_view() , name="login-page"),

]
