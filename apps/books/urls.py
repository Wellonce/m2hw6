from django.urls import path

from apps.books.views import home_view

urlpatterns = [
    path('homepage/', home_view, name="home"),

]
