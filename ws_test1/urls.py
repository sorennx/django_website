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
    re_path(r'^projects/uniprojects/tablesandforms$', views.tablesAndForms, name='tablesandforms')
]
