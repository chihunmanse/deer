from services.models import ForbiddenArea

# 서비스지역외 반납 패널티
class OutsidePenalty:
    def __init__(self, area, end_point):
        self.area              = area
        self.end_point         = end_point
        self.penalty           = 0
        self.PENAlTY_PER_METER = 10

    def calculate_penalty(self):
        if not self.area.area_boundary.within(self.end_point):
            distance     = round(self.area.area_boundary.distance(self.end_point) * 100000)
            self.penalty = distance * self.PENAlTY_PER_METER

        return self.penalty

# 반납금지지역 반납 패널티
class ForbiddenAreaPenalty:
    def __init__(self, area, end_point):
        self.area              = area
        self.end_point         = end_point
        self.penalty           = 0
        self.FORBIDDEN_PANALTY = 6000

    def calculate_penalty(self):
        if ForbiddenArea.objects.filter(area = self.area, forbidden_boundary__contains = self.end_point).exists():
            self.penalty = self.FORBIDDEN_PANALTY
        
        return self.penalty