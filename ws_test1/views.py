
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'pai_page/index.html')

def detail(request, question_id):
    return render(request,'')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def home(request):
    my_dict = {"title":'Home'}
    return render(request, 'main_page/home.html', my_dict)

def projects(request):
    my_dict = {"title": 'Projects'}
    return render(request,'main_page/projects.html', my_dict)

def contact(request):
    my_dict = {"title": 'Contact'}
    return render(request, 'main_page/contactinfo.html', my_dict)

