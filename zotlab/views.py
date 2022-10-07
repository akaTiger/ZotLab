from django.http import HttpResponse

def webTitle(request):
	return HttpResponse("Welcome to ZotLab!")
