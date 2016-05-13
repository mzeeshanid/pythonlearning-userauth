from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Category


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_title',)
