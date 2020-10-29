from django.shortcuts import render, redirect
from .models import MainModel
from .forms import DisplayForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	if request.method == "POST":
		add = DisplayForm(request.POST)
		if add.is_valid():
			add.save()
			add = DisplayForm()
	else:
		add = DisplayForm()
	show = MainModel.objects.all()
	context = {'show':show, 'add':add}
	return render(request, 'main/home.html', context)


# def delete(request, id):
# 	 MainModel.objects.get(id=id).delete()
# 	 return redirect('/')

def delete(request, id):
	if request.method == "POST":
		get = MainModel.objects.get(id=id)
		get.delete()
		return redirect('/')
	else:
		get = MainModel.objects.get(id=id)
	context = {'get':get}
	return render(request, 'main/delete.html', context)

def update(request, id):
	if request.method == "POST":
		form = MainModel.objects.get(id=id)
		add = DisplayForm(data=request.POST, instance=form)
		if add.is_valid():
			add.save()
			return redirect('profile')
	else:
		form = MainModel.objects.get(id=id)
		add = DisplayForm(instance=form)
	context = {'form': add}
	return render(request, 'main/update.html', context)

# def customRegistrationForm(request):
# 	if request.method == "POST":
# 		form = CustomUserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			new_user = form.save(commit = False)
# 			new_user.set_password(form.cleaned_data['password1'])
# 			new_user.save()
# 	else: 
# 		form = CustomUserRegistrationForm()
# 	context = {'form':form}
# 	return render(request, 'registration/register.html', context)


def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = CustomUserCreationForm()
	context = {'form':form}
	return render(request, 'registration/register.html', context)

@login_required(login_url='login')
def profile(request):
	if request.method == "POST":
		add = DisplayForm(request.POST)
		if add.is_valid():
			add.save()
			add = DisplayForm()
	else:
		add = DisplayForm()

	show = MainModel.objects.filter(user=request.user)
	context = {'show':show, 'add':add}
	return render(request, 'main/profile.html', context)


