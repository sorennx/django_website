from django.urls import re_path
from . import views
urlpatterns = [
    #re_path(r'^$',views.home, name='index'),
    # ex: /polls/5/
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    re_path(r'^$', views.home, name='home'),
    re_path(r'^projects/$', views.projects, name='projects'),
    re_path(r'^contact/$', views.contact, name='contact'),

    re_path(r'^wstest/$', views.index, name='index'),

    #university projects:
    re_path(r'^projects/uniprojects/$',views.universityProjects, name='uniprojects'),
    re_path(r'^projects/uniprojects/tablesandforms$', views.tablesAndForms, name='tablesandforms'),
    re_path(r'^projects/uniprojects/tablesandforms/tables$', views.tablesAndForms_tables, name='tablesandforms'),
    re_path(r'^projects/uniprojects/tablesandforms/forms$', views.tablesAndForms_forms, name='tablesandforms'),
    re_path(r'^projects/uniprojects/tablesandforms/galeria$', views.galeria,name='tablesandforms'),
    re_path(r'^projects/uniprojects/tablesandforms/walidacja$',views.walidacja,name='tablesandforms'),
    re_path(r'^projects/uniprojects/tablesandforms/dotacje$',views.dotacje,name='tablesandforms'),

    #other stuff:
    re_path(r'^projects/uniprojects/pizzacreator/$', views.pizzaCreator,name='pizzacreator'),
    re_path(r'^projects/uniprojects/other/maths/$', views.mathsStuff, name='mathsstuff'),
    re_path(r'^projects/uniprojects/other/css-selectors/$', views.cssSelectors, name='cssselectors'),
    #hobby projects:
    re_path(r'^projects/hobbyprojects/$', views.hobbyprojects, name='hobbyprojects'),
    re_path(r'^projects/hobbyprojects/wordlepl/$', views.wordlepl, name='hobbyprojects'),


]
