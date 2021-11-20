from services.models import ParkingZone

# 파킹존 반납 할인
class ParkingzoneDiscount:
    def __init__(self, area, end_point, use_fee):
        self.area      = area
        self.end_point = end_point
        self.use_fee   = use_fee
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

# 특정 킥보드 파킹존 반납 할인
class LuckykicboardDiscount:
    def __init__(self, area, end_point, use_fee, kickboard):
        self.area      = area
        self.end_point = end_point
        self.use_fee   = use_fee
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
