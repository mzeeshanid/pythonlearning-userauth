"""userauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from snippets.views import snippet_detail
from snippets.views import snippet_list

from rango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rango/$', views.home, name='home'),
    url(r'^rango/login/$', views.user_login, name='login'),
    url(r'^rango/logout/$', views.user_logout, name='logout'),
    url(r'^rango/register/$', views.register, name='register'),
    url(r'^rango/categories/$', views.categories, name='categories'),
    url(r'^rango/categories/add/$', views.add_category, name='addcategory'),
    url(r'^snippet/snippets/$', snippet_list),
    url(r'^snippet/snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]
