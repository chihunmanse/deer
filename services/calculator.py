# 총 할인액 계산
class DiscountCalculation:
    def __init__(self, discounts):
        self.discount  = 1
        self.discounts = discounts
    
    def calculate_discount(self):
        for discount in self.discounts:
            self.discount *= discount.calculate_discount()

        return self.discount

# 총 쿠폰액 계산
class CouponCalculation:
    def __init__(self, coupons):
        self.coupon  = 0
        self.coupons = coupons
    
    def calculate_coupon(self):
        for coupon in self.coupons:
            self.coupon += coupon.calculate_coupon()

        return self.coupon

# 총 벌금액 계산
class PenaltyCalculation:
    def __init__(self, penalties):
        self.penalty   = 0
        self.penalties = penalties
    
    def calculate_penalty(self):
        for penalty in self.penalties:
            self.penalty += penalty.calculate_penalty()
        
        return self.penalty