from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

class GameUser(models.Model):
    """
    用户信息
    """
    name = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    status = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Team(models.Model):
    """
    队伍信息
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    def __str__(self):
        return [self.name,self.owner]

class Member(models.Model):
    """
    成员信息
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    memberclass = models.CharField(max_length=10)
    ability1 = models.CharField(max_length=10)
    ability2 = models.CharField(max_length=10)
    ability3 = models.CharField(max_length=10)
    skill1 = models.CharField(max_length=10)
    skill2 = models.CharField(max_length=10)
    skill3 = models.CharField(max_length=10)
    skill4 = models.CharField(max_length=10)
    def __str__(self):
        return self.team