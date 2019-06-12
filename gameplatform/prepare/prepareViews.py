from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

import json

def index(request):
	return render(request,'index.html')

	
def logIn(request):
	if request.method == "GET":
		ret = {"logInStatus":1}
		return HttpResponse(json.dumps(ret))