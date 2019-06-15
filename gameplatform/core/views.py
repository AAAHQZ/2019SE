from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import GameUser,Race,Skill,Item,Team
import hashlib
# from django.views.decorators.csrf import csrf_exempt

import json

def index(request):
	return render(request,'index.html')

def battle(request):
	return render(request,'battle.html')
	
def logIn(request):
	if request.method == "GET":
		retstatus = 2
		userID=request.GET.get('userID')
		userPassword=request.GET.get('userPassword')
		try:
			GUPW = GameUser.objects.get(userID=userID)
		except:
			ret =  {"logInStatus":retstatus}
			return HttpResponse(json.dumps(ret))
		if(retstatus):    
			md5 = hashlib.md5()
			md5.update(userPassword.encode())
			result = md5.hexdigest()
			if result == GUPW.userPassword:
				retstatus = 1
			else:
				retstatus = 3
		ret = {"logInStatus":retstatus}
		return HttpResponse(json.dumps(ret))

def signUp(request):
	if request.method == "GET":
		retstatus = 0
		userID=request.GET.get('userID')
		userPassword=request.GET.get('userPassword')
		try:
			GUPW = GameUser.objects.get(userID=userID)
		except:
			retstatus = 1 
		if(retstatus):    
			md5 = hashlib.md5()
			md5.update(userPassword.encode())
			result = md5.hexdigest()
			newGU = GameUser(userID=userID,userPassword=result,userStatus='signed')
			newGU.save()
		ret = {"signUpStatus":retstatus}
	return HttpResponse(json.dumps(ret))

def getMonsterData(request):
	if request.method == "GET":
		monsterList = []
		races = Race.objects.all()
		for race in races:
			racedict = model_to_dict(race)
			monsterList.append(racedict)
		# print(monsterList)
		ret = {'monsterList':monsterList}
	return HttpResponse(json.dumps(ret))

def getSkillData(request):
	if request.method == "GET":
		skillList = []
		skills = Skill.objects.all()
		for skill in skills:
			skilldict = model_to_dict(skill)
			skillList.append(skilldict)
		ret = {'skillList':skillList}
	return HttpResponse(json.dumps(ret))


def getItemData(request):
	if request.method == "GET":
		ItemList = []
		items = Item.objects.all()
		for item in items:
			itemdict = model_to_dict(item)
			ItemList.append(itemdict)
		ret = {'skillList':ItemList}
	return HttpResponse(json.dumps(ret))
    
def getUserTeam(request):
    if request.method == "GET":
        teamList = []
        userID = request.GET.get('userID')
        try:
            teamOwner = GameUser.objects.get(userID=userID)
        except:
            ret = {'teamList':teamList}
            return HttpResponse(json.dumps(ret))
        teams = Team.objects.fliter(teamOwner=teamOwner)
        for team in teams:
            teamdict = model_to_dict(team)
            teamList.append(teamdict)
        ret = {'teamList':teamList}
    return HttpResponse(json.dumps(ret))        

# def returnUserTeam(request):

