"""django_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^',include('ws_test1.urls')),
    re_path(r'^wstest/', include('ws_test1.urls')),

    re_path(r'^home/', include('ws_test1.urls')),
    re_path(r'^projects/', include('ws_test1.urls')),
    re_path(r'^contact/', include('ws_test1.urls')),

    #university projects:
    re_path(r'^projects/uniprojects/',include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/tables', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/forms', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/pizzacreator/', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/other/maths/',include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/other/css-selectors/', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/galeria', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/walidacja', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/dotacje', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/tablesandforms/formscalcs', include('ws_test1.urls')),
    re_path(r'^projects/uniprojects/responsive/rwd', include('ws_test1.urls')),

]