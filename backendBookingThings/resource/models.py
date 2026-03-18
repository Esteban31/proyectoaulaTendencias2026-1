from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=50)
    resourcetype = models.CharField(max_length=30)  # SALA/EQUIPO/ESPACIO
    description = models.CharField(max_length=200)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20) #ACTIVO/INACTIVO/MANTENIMIENTO
    availableSchedule = models.JSONField()
    
    def __str__(self):
        return self.name