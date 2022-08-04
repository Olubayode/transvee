from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_user(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home-1')
		else:
			messages.success(request, ('There was an Error Logging in, Try Again!!!'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Were Logged Out!!!'))
	return redirect('home')



@csrf_exempt
def register_user(request):
	if request.method == "POST":
		forms = UserCreationForm(request.POST)
		if forms.is_valid():
			forms.save()
			username = forms.cleaned_data['username']
			password = forms.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			
			return redirect('home-1')
	else:
		forms = UserCreationForm()
	return render(request, 'authenticate/register_user.html',{'forms': forms })



