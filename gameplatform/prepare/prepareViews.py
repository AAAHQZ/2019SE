from django.shortcuts import render
from django.http import HttpResponse
from .models import GameUser
import hashlib
# from django.views.decorators.csrf import csrf_exempt

import json

def index(request):
	return render(request,'index.html')

	
def logIn(request):
	if request.method == "GET":
		retstatus = 2
		userID=request.GET.get('userID')
		userPassword=request.GET.get('userPassword')
		try:
			GUPW = GameUser.objects.get(userName=userID)
		except:
			ret =  {"signUpStatus":retstatus}
			return HttpResponse(json.dumps(ret))
		if(retstatus):    
			md5 = hashlib.md5()
			md5.update(userPassword.encode())
			result = md5.hexdigest()
			if result == GUPW.userPassword:
				retstatus = 1
			else:
				retstatus = 3
		ret = {"signUpStatus":retstatus}
		return HttpResponse(json.dumps(ret))

def signUp(request):
	if request.method == "GET":
		retstatus = 0
		userID=request.GET.get('userID')
		userPassword=request.GET.get('userPassword')
		try:
			GUPW = GameUser.objects.get(userName=userID)
		except:
			retstatus = 1 
		if(retstatus):    
			md5 = hashlib.md5()
			md5.update(userPassword.encode())
			result = md5.hexdigest()
			newGU = GameUser(userName=userID,userPassword=result,userStatus='signed')
			newGU.save()
		ret = {"signUpStatus":retstatus}
	return HttpResponse(json.dumps(ret))
