from django.db import models

# Create your models here.
class ClientConfigurations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    commisionTolerance = models.FloatField()
    grossAmountTolerance = models.FloatField()

    def __str__(self):
        return self.name
    
class Roles(models.Model):
    roleId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    roleId = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="users")

class Requests(models.Model):
    id = models.AutoField(primary_key=True)
    requestTime = models.DateTimeField()
    requesterId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="requester_requests", null=True)
    verifierId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="verifier_requests", null=True)
    clientConfigId = models.ForeignKey(ClientConfigurations, on_delete=models.CASCADE, related_name="requests", null=True)
    grossAmountToleranceTo = models.FloatField()
    commisionToleanceTo = models.FloatField()

class AuditLogs(models.Model):
    id = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField()
    statusId = models.IntegerField()
    requestId = models.IntegerField()
    requesterId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="requester_audit_logs", null= True)
    verifierId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="verifier_audit_logs", null=True)
    clientConfigId = models.ForeignKey(ClientConfigurations, on_delete=models.CASCADE, related_name="audit_logs", null=True)
    grossAmountToleranceFrom = models.FloatField(null=True)
    grossAmountToleranceTo = models.FloatField(null=True)
    commisionToleranceFrom = models.FloatField(null=True)
    commisionToleanceTo = models.FloatField(null=True)
