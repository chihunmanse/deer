from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    phone_number = models.CharField(max_length = 20, unique = True)
    password     = models.CharField(max_length = 100)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.phone_number