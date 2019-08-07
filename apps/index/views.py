from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    def get(self,request):
        return  render(request, "index.html")


class XinView(View):
    def get(self,request):
        return  render(request, "xin.html")


class LoveView(View):
    def get(self,request):
        return  render(request, "love.html")


class DycView(View):
    def get(self,request):
        return  render(request, "dyc.html")


class XcView(View):
    def get(self,request):
        return  render(request, "xc.html")


class ShView(View):
    def get(self,request):
        return  render(request, "sh.html")


class XwView(View):
    def get(self,request):
        return  render(request, "all/home.html")


class XwView1(View):
    def get(self,request):
        return  render(request, "all/main.html")


class XwView2(View):
    def get(self,request):
        return  render(request, "all/index1.html")


class XwView3(View):
    def get(self,request):
        return  render(request, "all/index2.html")


class XwView4(View):
    def get(self,request):
        return  render(request, "all/index3.html")

class XwView5(View):
    def get(self,request):
        return  render(request, "all/index4.html")

class XwView6(View):
    def get(self,request):
        return  render(request, "all/index5.html")


