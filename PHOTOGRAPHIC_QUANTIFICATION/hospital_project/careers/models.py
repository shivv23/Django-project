from django.db import models

class positions(models.Model):
    positionname = models.CharField(max_length=255)
    recruitingManager = models.CharField(max_length=255)
    hiringManager = models.CharField(max_length=255)
    openingDate = models.DateField(null=True)
    closedDate = models.DateField(null=True)
    notes = models.CharField(max_length=500)
    status = models.IntegerField(null=True)
    department = models.CharField(max_length=500)
    baseSalary = models.IntegerField(null=True)
    behaviouranalyst = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.positionname} {self.baseSalary} {self.department}"
