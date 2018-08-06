from django.db import models

# Create your models here.
"""
           用户表

字段         类型        描述

username   string      用户账号
passwd     string      密码（加密存储）      
name       string      用户姓名
profile    string      头像地址
userType   Integer     用户身份

"""
class user(models.Model):

    username  = models.CharField(max_length=30)
    passwd    = models.CharField(max_length=32)
    name      = models.CharField(max_length=10)
    profile   = models.CharField(max_length=100)
    userType  = models.IntegerField(max_length=1)
    isDelete  = models.BooleanField(default=False)

    @classmethod
    def userObject(cls,username,passwd,name,profile,userType):
        userNew = user()
        userNew.username = username
        userNew.name = name
        userNew.passwd = passwd
        userNew.profile = profile
        userNew.userType = userType
        userNew.save()
        return userNew

"""
            tokon表
字段          类型        描述

userID       string      用户标识
token        string      token值
domain       string      有效时间 


"""
class userToken(models.Model):

    username  = models.ForeignKey(user,related_name='username')
    token     = models.CharField(max_length=32)
    domain    = models.CharField(max_length=30)

    @classmethod
    def userTokenObject(cls,username,token,domain=None):
        new = userToken()
        new.username = username
        new.token = token
        new.domain = domain
        new.save()
        return new


"""
             群组表

字段           类型           描述
groupID      string          群组ID
name         string          群组名称
owner        string          创建者
member       array           群组成员

"""
class group(models.Model):

    groupID   = models.CharField(max_length=20)
    name      = models.CharField(max_length=20)
    owner     = models.ForeignKey(user,related_name='username')
    member    = models.CharField(max_length=1000)
    isDelete    = models.BooleanField(default=False)

    @classmethod
    def groupObject(cls,groupID,name,owner,member=None):
        new = group()
        new.groupID = groupID
        new.name = name
        new.owner = owner
        new.member = member
        new.save()
        return new

"""
             群组表

字段           类型           描述

checkID        string        签到标识
groupID        string        签到群组
startUpTime    string        开始时间
duration       Integer       持续时间
enable         boolean       签到开关
results        array         签到成员
members        array         签到开启时群组成员         

"""
class check(models.Model):

    checkID     = models.CharField(max_length=20)
    groupID     = models.ForeignKey(group)
    startUpTime = models.CharField(max_length=30)
    duration    = models.IntegerField(max_length=5)
    enable      = models.BooleanField(default=False)
    results     = models.CharField(max_length=1000)
    members     = models.CharField(max_length=1000)

    @classmethod
    def checkObject(cls,checkID,groupID,startUpTime=None,duration=None,enable=None,results=None,members=None):
        new = check()
        new.checkID = checkID
        new.groupID = groupID
        new.startUpTime = startUpTime
        new.duration = duration
        new.enable = enable
        new.results = results
        new.members = members
        new.save()
        return new


"""
             群组表

字段           类型           描述

planID        string         计划ID
groupID       string         计划作用群组ID
startUpTime   string         计划开始时间
duration      Integer        计划持续时间
repeat        string         计划作用域
enable        boolean        计划开关


"""


class checkPlan(models.Model):

    planID      = models.CharField(max_length=20)
    groupID     = models.ForeignKey(group)
    startUpTime = models.CharField(max_length=30)
    duration    = models.IntegerField(max_length=5)
    repeat      = models.CharField(max_length=20)
    enable      = models.BooleanField(default=False)
    isDelete    = models.BooleanField(default=False)

    @classmethod
    def checkPlanObejct(cls,planID,groupID,startUpTime=None,duration=None,repeat=None,enable=False):
        new = checkPlan()
        new.planID = planID
        new.groupID = groupID
        new.startUpTime = startUpTime
        new.duration = duration
        new.repeat =repeat
        new.enable = enable
        new.save()
        return new


