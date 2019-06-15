from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

class GameUser(models.Model):
    """
    用户信息
    """
    objects = models.Manager() 
    userID = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)
    userStatus = models.CharField(max_length=10)
    def __str__(self):
        return self.userID

class Item(models.Model):
    """
    道具信息
    """
    objects = models.Manager() 
    itemName = models.CharField(max_length=100)
    itemType = models.IntegerField()
    itemAttribute1 = models.IntegerField()
    itemAttribute2 = models.IntegerField()

class Race(models.Model):
    """
    种族信息
    """
    objects = models.Manager() 
    raceName = models.CharField(max_length=100)
    racePhoto = models.CharField(max_length=100)
    raceType = models.CharField(max_length=100,default='电')
    raceHp = models.IntegerField()
    raceAtk = models.IntegerField()
    raceDef = models.IntegerField()
    raceSpa = models.IntegerField()
    raceSpd = models.IntegerField()
    raceSpe = models.IntegerField()
    raceability = models.CharField(max_length=100)

class Skill(models.Model):
    """
    技能信息
    """
    objects = models.Manager() 
    skillType = models.CharField(max_length=100)
    skillClass = models.CharField(max_length=100,default='物理')
    skillPhoto = models.CharField(max_length=100)
    skillPower = models.IntegerField()

class Team(models.Model):
    """
    队伍信息
    """
    objects = models.Manager() 
    teamName = models.CharField(max_length=100)
    teamOwner = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    teamItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return [self.teamName,self.teamOwner]

class Member(models.Model):
    """
    成员信息
    """
    objects = models.Manager() 
    memberTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    memberRace = models.ForeignKey(Race, on_delete=models.CASCADE)
    def __str__(self):
        return self.memberTeam

class MemberSkill(models.Model):
    objects = models.Manager() 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
