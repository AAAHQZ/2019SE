from .models import GameUser
import hashlib

def signup(userID, userPassword):
    ret = 0
    try:
        GUPW = GameUser.objects.get(userID=userID)
    except:
        ret = 1 
    if(ret):    
        md5 = hashlib.md5()
        md5.update(userPassword.encode())
        result = md5.hexdigest()
        newGU = GameUser(userID=userID,userPassword=userPassword,userStatus='signed')
        newGU.save()
    return ret