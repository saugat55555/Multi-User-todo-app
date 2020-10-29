from django import forms
from .models import MainModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DisplayForm(forms.ModelForm):
	class Meta:
		model = MainModel
		fields = ('task', 'user',)

# class CustomUserRegistrationForm(forms.ModelForm):
# 	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
# 	password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email',)

# 		def clean_password2(self):
# 			cd = self.cleaned_data
# 			if cd['password1'] != cd['password2']:
# 				raise forms.ValidationError("Password don't match")
# 			return cd['password2']

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email']
			