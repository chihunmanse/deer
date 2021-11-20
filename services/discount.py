from services.models import ParkingZone

# 파킹존 반납 할인 - 30% 
class ParkingzoneDiscount:
    def __init__(self, area, end_point):
        self.area      = area
        self.end_point = end_point
        self.discount  = 1
        
    def calculate_discount(self):
        parkingzones = ParkingZone.objects.filter(area = self.area)

        for parkingzone in parkingzones:
            center = parkingzone.parking_center
            radius = parkingzone.parking_radius / 100000
            circle = center.buffer(radius)

            if self.end_point.within(circle):
               self.discount = 0.7
        
        return self.discount

# 특정 킥보드 파킹존 반납 할인 - 100%
class LuckykicboardDiscount:
    def __init__(self, area, end_point, kickboard):
        self.area      = area
        self.end_point = end_point
        self.kickboard = kickboard
        self.discount  = 1
        
    def calculate_discount(self):
        if self.kickboard.event_id == 1:
            parkingzones = ParkingZone.objects.filter(area = self.area)

            for parkingzone in parkingzones:
                center = parkingzone.parking_center
                radius = parkingzone.parking_radius / 100000
                circle = center.buffer(radius)

                if self.end_point.within(circle):
                    self.discount = 0
        
        return self.discount

# 출근시간대 대여 할인 - 10%
class WorkingtimeDiscount:
    def __init__(self, start_at):
        self.start_hour = int(start_at.strftime('%H'))
        self.discount   = 1
        
    def calculate_discount(self):
        if self.start_hour in [7, 8, 9]:
            self.discount = 0.9
        
        return self.discount

# 주말 21시 이후 할인 - 10%
class WeekendDiscount:
    def __init__(self, start_at):
        self.start_day  = start_at.strftime('%A')
        self.start_hour = int(start_at.strftime('%H'))
        self.discount   = 1
        
    def calculate_discount(self):
        if self.start_day in ['Saturday', 'Sunday'] and 21 <= self.start_hour:
            self.discount = 0.9
        
        return self.discount
