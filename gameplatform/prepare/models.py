from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

class GameUser(models.Model):
    """
    用户信息
    """
    userName = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)
    userStatus = models.CharField(max_length=5)
    def __str__(self):
        return self.userName

class Item(models.Model):
    """
    道具信息
    """
    itemName = models.CharField(max_length=100)
    itemType = models.IntegerField()
    itemAttribute1 = models.IntegerField()
    itemAttribute2 = models.IntegerField()

class Race(models.Model):
    """
    种族信息
    """
    raceName = models.CharField(max_length=100)
    racePhoto = models.CharField(max_length=100)
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
    skillType = models.CharField(max_length=100)
    skillPhoto = models.CharField(max_length=100)
    skillPower = models.IntegerField()

class Team(models.Model):
    """
    队伍信息
    """
    teamName = models.CharField(max_length=100)
    teamOwner = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    teamItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return [self.teamName,self.teamOwner]

class Member(models.Model):
    """
    成员信息
    """
    memberTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    memberRace = models.ForeignKey(Race, on_delete=models.CASCADE)
    def __str__(self):
        return self.memberTeam

class MemberSkill(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
