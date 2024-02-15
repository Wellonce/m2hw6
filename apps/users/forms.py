from django import forms
from django.core.exceptions import ValidationError

from apps.users.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))
    confirm_password = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))
    avatar = forms.FileField()

    def save(self, commit=True):
        user = super().save(commit)
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            user.set_password(password)
            user.save()
        else:
            raise ValidationError ("Passwords must match")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=28, widget=forms.TextInput(attrs={"class": "form-control", "id": "username"}))
    password = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "password", "type": "password"}))