import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","deer.settings")

django.setup()

import random

from services.models import *
from users.models    import User
from django.db       import transaction

from core.models     import TimeStampModel
from django.contrib.gis.geos import Polygon, Point, MultiPoint

with transaction.atomic():
    Area.objects.create(area_center = Point((37.559260, 127.073697)),
    area_boundary = Polygon(((37.559260, 127.073697), (37.549197, 127.068847), (37.548049, 127.074528), (37.556847, 127.079042), (37.559260, 127.073697))),
    area_coords = MultiPoint(Point(37.559260, 127.073697), Point(37.549197, 127.068847), Point(37.548049, 127.074528), Point(37.556847, 127.079042)))
    ForbiddenArea.objects.create(area_id = 1, 
        forbidden_boundary = Polygon(((37.552644, 127.073592), (37.552134, 127.072820), (37.550611, 127.074515), (37.551391, 127.075596), (37.552644, 127.073592))), \
        forbidden_coords = MultiPoint(Point(37.552644, 127.073592), Point(37.552134, 127.072820), Point(37.550611, 127.074515), Point(37.551391, 127.075596)))
    
    ParkingZone.objects.create(area_id = 1, parking_center = Point((37.555222, 127.075695)), parking_radius = 30)
    ParkingZone.objects.create(area_id = 1, parking_center = Point((37.550365, 127.071446)), parking_radius = 25)
    




# class Area(TimeStampModel) :
#     area_center   = geomodels.PointField()
#     area_boundary = geomodels.PolygonField()
#     area_coords   = geomodels.MultiPointField()
    
#     class Meta :
#         db_table = 'areas'

# class ParkingZone(TimeStampModel) :
#     area           = models.ForeignKey('Area', on_delete=models.CASCADE)
#     parking_center = geomodels.PointField()
#     parking_radius = models.DecimalField(max_digits=20, decimal_places=10)
    
#     class Meta :
#         db_table = 'parking_zones'
    
# class ForbiddenArea(TimeStampModel) :
#     area               = models.ForeignKey('Area', on_delete=models.CASCADE)
#     forbidden_boundary = geomodels.PolygonField()
#     forbidden_coords   = geomodels.MultiPointField()
    
#     class Meta :
#         db_table = 'forbidden_areas'