"""qx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from index.views import IndexView,XinView,LoveView,DycView,XcView,ShView
from index.views import XwView,XwView1,XwView2,XwView3,XwView4,XwView5,XwView6

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index$', IndexView.as_view(), name="index"),
    url(r'^xin/$', XinView.as_view(), name="xin"),
    url(r'^love/$', LoveView.as_view(), name="love"),
    url(r'^dyc/$', DycView.as_view(), name="dyc"),
    url(r'^xc/$', XcView.as_view(), name="xc"),
    url(r'^sh/$', ShView.as_view(), name="sh"),

    url(r'^xw/$', XwView.as_view(), name="xw"),
    url(r'^xw1/$', XwView1.as_view(), name="xw1"),
    url(r'^xw2/$', XwView2.as_view(), name="xw2"),
    url(r'^xw3/$', XwView3.as_view(), name="xw3"),
    url(r'^xw4/$', XwView4.as_view(), name="xw4"),
    url(r'^xw5/$', XwView5.as_view(), name="xw5"),
    url(r'^xw6/$', XwView6.as_view(), name="xw6"),



]
