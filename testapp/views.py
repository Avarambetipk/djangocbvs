from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
class HelloWordView(View):
    def get(self,request):
        return HttpResponse()
class TemplateCBV(TemplateView):
    template_name = 'testapp/results.html'


