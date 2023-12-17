from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'username']

class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Введите логин', widget=forms.TextInput)
    email = forms.EmailField(label='Введите Email', max_length=254)
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Введите повторно пароль', widget=forms.PasswordInput)
    avatar = forms.ImageField(label='Предоставьте ваше фото', widget=forms.ClearableFileInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'avatar']