
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'pai_page/tablesandforms/index.html')

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


#Uni projects:

def universityProjects(request):
    my_dict = {"title": 'University Projects'}
    return render(request, 'main_page/uniprojects.html', my_dict)

#tablesAndForms

def tablesAndForms(request):
    my_dict = {"title:": 'Tables and Forms'}
    return render(request, 'pai_page/tablesandforms/index.html', my_dict)

def tablesAndForms_tables(request):
    my_dict={"title:": "Tables and Froms - tables"}
    return render(request, 'pai_page/tablesandforms/tabele.html', my_dict)

def tablesAndForms_forms(request):
    my_dict={"title:": "Tables and Froms - forms"}
    return render(request, 'pai_page/tablesandforms/formularze.html', my_dict)

def galeria(request):
    return render(request, 'pai_page/tablesandforms/galeria.html', {})

def walidacja(request):
    return render(request,'pai_page/tablesandforms/walidacja.html',{})

def dotacje(request):
    return render(request,'pai_page/tablesandforms/dotacje.html',{})

def formscalcs(request):
    return render(request, 'pai_page/tablesandforms/formscalcs.html',{})

def responsive(request):
    return render(request,'pai_page/responsive/rwd.html',{})

#other stuff
def mathsStuff(request):
    return render(request,'pai_page/other/maths.html', {})

def cssSelectors(request):
    return render(request,'pai_page/other/css-selectors.html', {})

def pizzaCreator(request):
    return render(request, 'pai_page/pizzacreator/pizzacreator.html', {})


#hobby projects:
def hobbyprojects(request):
    my_dict = {"title": 'Hobby Projects'}
    return render(request, 'main_page/hobbyprojects.html', my_dict)

def wordlepl(request):
    my_dict = {"title": 'Wordlepl'}
    return render(request, 'hobbyprojects/wordlepl/index.html', my_dict)


