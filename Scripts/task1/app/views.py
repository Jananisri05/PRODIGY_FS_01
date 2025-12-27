from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.forms import SignupForm,LoginForm
def signup_view(request):
    if request.method=="POST":
        form= SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data["username"],email=form.cleaned_data["email"],password=form.cleaned_data["password"])
            return redirect('/login/')
        else:
            print(form.errors)
    else:
        form=SignupForm()
    return render(request,"app/signup.html",{"form":form})
    
def login_view(request):
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/dashboard/')
    else:
        form=LoginForm()
    return render(request,"app/login.html",{"form":form})
@login_required
def dashboard_view(request):
    return render(request,"app/dashboard.html")
def logout_view(request):
    logout(request)
    return redirect('/login/')



