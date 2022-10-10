from django.http import HttpResponse
from django.shortcuts import render

def webTitleHtml(request):
	context = {}
	context['title'] = 'ZOT LAB !!'
	return render(request, 'home.html', context)
