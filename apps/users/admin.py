from django.contrib import admin
from .models import User, BookShelf
# Register your models here.
admin.site.register([ User, BookShelf])