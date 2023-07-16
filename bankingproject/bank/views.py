from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from bank.forms import AccountForm


# Create your views here.
def home(request):
	return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bank:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data ['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("bank:create")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", context={"form":form})

def logout(request):
    auth.logout(request)
    return redirect('bank:login')
def create(request):
	return render(request,'create.html')

def account(request):
    account = AccountForm()
    return render(request,"account.html",context={'form':account})
# def account(request):
# 	return render(request,'account.html')