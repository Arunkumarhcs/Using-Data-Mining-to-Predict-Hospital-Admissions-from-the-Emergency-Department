"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from admins import views as admin_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$', admin_views.index, name="index"),
    url('user/register', admin_views.register, name="register"),
    url('user/userpage', admin_views.userpage, name="userpage"),
    url('user/mydetails', admin_views.mydetails, name="mydetails"),
    url('user/upload_page', admin_views.upload_page, name="upload_page"),
    url('user/search_patent', admin_views.search_patent, name="search_patent"),
    url('user/particular_patent', admin_views.particular_patent, name="particular_patent"),
    url('user/dataset', admin_views.dataset, name="dataset"),
    url('user/chart_page', admin_views.chart_page, name="chart_page"),
]
