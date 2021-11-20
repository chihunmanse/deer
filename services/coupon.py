from services.models import Service

# 30분 이내 재대여 기본요금 쿠폰
class LatestuseCoupon:
    def __init__(self, area, user, start_at):
        self.area     = area
        self.user     = user
        self.start_at = start_at
        self.coupon   = 0

    def calculate_coupon(self):
        last_service = Service.objects.filter(user = self.user).order_by('-end_time').first()
        
        if last_service:
            last_time = last_service.end_time

            if (self.start_at - last_time).days * 1440 + (self.start_at - last_time).seconds / 60 <= 30:
                print((self.start_at - last_time).seconds / 60)
                self.coupon = self.area.basic_fee
        
        return self.coupon

# 첫 이용시 1000원 쿠폰
class FirstuseCoupon:
    def __init__(self, user):
        self.user   = user
        self.coupon = 0

    def calculate_coupon(self):
        if not Service.objects.filter(user = self.user).exists():
            self.coupon = 1000
        
        return self.coupon

# 크리스마스에 이용시 1000원 쿠폰
class ChristmasCounpon:
    def __init__(self, start_at):
        self.start_day = start_at.strftime('%m-%d')
        self.coupon    = 0

    def calculate_coupon(self):
        if self.start_day == '12-25':
            self.coupon = 1000
        
        return self.coupon
