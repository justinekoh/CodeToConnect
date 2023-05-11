from django.db import models

# Create your models here.
class ClientConfigurations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    commisionTolerance = models.FloatField()
    grossAmountTolerance = models.FloatField()

    def __str__(self):
        return self.name
    
class Roles(models.Model):
    roleId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    roleId = models.ForeignKey(Roles)

class Requests(models.Model):
    id = models.IntegerField(primary_key=True)
    requestTime = models.DateTimeField()
    requesterId = models.ForeignKey(Users)
    verifierId = models.ForeignKey(Users)
    clientConfigId = models.ForeignKey(ClientConfigurations)
    grossAmountToleranceTo = models.FloatField()
    commisionToleanceTo = models.FloatField()

class AuditLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    createdAt = models.DateTimeField()
    statusId = models.IntegerField()
    requestId = models.ForeignKey(Requests)
    requesterId = models.ForeignKey(Users)
    verifierId = models.ForeignKey(Users)
    clientConfigId = models.ForeignKey(ClientConfigurations)
    grossAmountToleranceFrom = models.FloatField()
    grossAmountToleranceTo = models.FloatField()
    commisionToleranceFrom = models.FloatField()
    commisionToleanceTo = models.FloatField()
