"""micalculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'mycalculadorapp.views.barra'),
    url(r'.*','mycalculadorapp.views.error'),
    url(r'^(\-?\d+)/suma/(\-?\d+)','mycalculadorapp.views.suma'),
    url(r'^(\-?\d+)/resta/(\-?\d+)','mycalculadorapp.views.resta'),
    url(r'^(\-?\d+)/multiplicacion/(\-?\d+)','mycalculadorapp.views.multiplicacion'),
    url(r'^(\-?\d+)/division/(\-?\d+)','mycalculadorapp.views.division'),
    url(r'^admin/', include(admin.site.urls)),
)
