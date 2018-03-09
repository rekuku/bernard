from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.template.response import TemplateResponse

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
    	return render(request, 'index.html', {})
        #return HttpResponse(self.greeting)