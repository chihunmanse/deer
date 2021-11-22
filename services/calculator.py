# 총 할인율 계산
class DiscountCalculation:
    def __init__(self, discounts):
        self.discount       = 1
        self.discounts      = discounts
        self.discount_names = []
    
    def calculate_discount(self):
        for discount in self.discounts:
            self.discount *= discount.calculate_discount()

        return self.discount
    
    def get_discount_name(self):
        for discount in self.discounts:
            self.discount = discount.calculate_discount()
            if self.discount < 1:
                self.discount_names.append(discount.get_discount_name())
        
        return self.discount_names

# 총 쿠폰액 계산
class CouponCalculation:
    def __init__(self, coupons):
        self.coupon       = 0
        self.coupons      = coupons
        self.coupon_names = []
    
    def calculate_coupon(self):
        for coupon in self.coupons:
            self.coupon += coupon.calculate_coupon()

        return self.coupon
    
    def get_coupon_name(self):
        for coupon in self.coupons:
            self.coupon = coupon.calculate_coupon()
            if self.coupon > 0:
                self.coupon_names.append(coupon.get_coupon_name())
        
        return self.coupon_names

# 총 패널티 계산
class PenaltyCalculation:
    def __init__(self, penalties):
        self.penalty       = 0
        self.penalties     = penalties
        self.penalty_names = []
    
    def calculate_penalty(self):
        for penalty in self.penalties:
            self.penalty += penalty.calculate_penalty()
        
        return self.penalty
    
    def get_penalty_name(self):
        for penalty in self.penalties:
            self.penalty = penalty.calculate_penalty()
            if self.penalty > 0:
                self.penalty_names.append(penalty.get_penalty_name())

        return self.penalty_names