from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View

def login(request):
    return render(request,'signup/New_login.html')
def new_student_signup(request):
    return render(request,'signup/new_student_signup.html')
def new_university_signup(request):
    return render(request,'signup/new_university_signup.html')