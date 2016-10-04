from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse 
from .models import Page


def index(request):
	page = Page.objects.all()
	return render(request, 'index.html',{'list':page})

def aboutus(request):
	return render(request, 'about-us.html',{'data':''})

def about_us_with_team_members(request):
	return render(request,'about-us-with-team-members.html')

def service(request):
	return render(request,'service.html')

def portfolio(request):
	return render(request , "portfolio.html")

def blogs(request):
	return render(request, 'blog.html')

def shop(request):
	return render(request,'shop.html')

def contact(request):
	return render(request,'contact-us.html')

def handler404(request):
	return render(request,'404.html')