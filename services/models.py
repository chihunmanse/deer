from django.db             import models
from django.contrib.gis.db import models as geomodels

from core.models           import TimeStampModel

class Area(TimeStampModel) :
    area_center   = geomodels.PointField()
    area_boundary = geomodels.PolygonField()
    area_coords   = geomodels.MultiPointField()
    
    class Meta :
        db_table = 'areas'

class ParkingZone(TimeStampModel) :
    area           = models.ForeignKey('Area', on_delete=models.CASCADE)
    parking_center = geomodels.PointField()
    parking_radius = models.DecimalField(max_digits=20, decimal_places=10)
    
    class Meta :
        db_table = 'parking_zones'
    
class ForbiddenArea(TimeStampModel) :
    area               = models.ForeignKey('Area', on_delete=models.CASCADE)
    forbidden_boundary = geomodels.PolygonField()
    forbidden_coords   = geomodels.MultiPointField()
    
    class Meta :
        db_table = 'forbidden_areas'

class KickBoard(TimeStampModel):
    name  = models.CharField(max_length = 50, unique = True)
    area  = models.ForeignKey('Area', on_delete=models.CASCADE, null = True)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)  

    class Meta:
        db_table = 'kickboards'
    
    def __str__(self):
        return self.name

class Service(TimeStampModel):
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()
    start_area = geomodels.PointField()
    end_area   = geomodels.PointField()
    fee        = models.PositiveIntegerField()
    user       = models.ForeignKey('users.User', on_delete = models.CASCADE)
    kickborad  = models.ForeignKey('Kickboard', on_delete = models.CASCADE)

    class Meta:
        db_table = 'services'
        
class Event(TimeStampModel) :
    name       = models.CharField(max_length=50)
    
    class Meta :
        db_table = 'events'
    
    def __str__(self) :
        return self.name