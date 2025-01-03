from django.db import models

class events(models.Model):
    eventname = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    note = models.CharField(max_length=500)
    
    


    
