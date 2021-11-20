import json
from json.decoder            import JSONDecodeError
from datetime                import datetime
from ctypes                  import ArgumentError

from django.views            import View
from django.http.response    import JsonResponse
from django.contrib.gis.geos import Point

from services.models         import KickBoard
from users.utils             import login_decorator
from services.calculator     import CouponCalculation, DiscountCalculation, PenaltyCalculation
from services.discount       import *
from services.penalty        import *
from services.coupon         import *

class CalculateView(View):
    @login_decorator
    def post(self, request):
        try:
            time_format    = '%Y-%m-%d %H:%M:%S'
            user           = request.user
            data           = json.loads(request.body)
            kickboard_name = data['kickboard_name']
            end_lat        = data['end_lat']
            end_lng        = data['end_lng']
            end_point      = Point((end_lat, end_lng))
            start_at       = datetime.strptime(data['start_at'], time_format)
            end_at         = datetime.strptime(data['end_at'], time_format)
            
            kickboard      = KickBoard.objects.select_related('area').get(name = kickboard_name)
            area           = kickboard.area
            use_time       = (end_at - start_at).days * 1440 + (end_at - start_at).seconds / 60
            use_fee        = area.basic_fee + area.minute_fee * use_time

            # 적용할 할인율 리스트
            discounts = [ParkingzoneDiscount(area, end_point), LuckykicboardDiscount(area, end_point, kickboard), WorkingtimeDiscount(start_at), WeekendDiscount(start_at)]

            # 적용할 쿠폰 리스트
            coupons   = [LatestuseCoupon(area, user, start_at), FirstuseCoupon(user), ChristmasCounpon(start_at)]

            # 적용할 패널티 리스트
            penalties = [OutsidePenalty(area, end_point), ForbiddenAreaPenalty(area, end_point)]

            discount  = DiscountCalculation(discounts).calculate_discount()
            penalty   = PenaltyCalculation(penalties).calculate_penalty()
            coupon    = CouponCalculation(coupons).calculate_coupon()
            
            total_fee = round(use_fee * discount - coupon + penalty)

            if use_time <= 1 or total_fee < 0:
                total_fee = 0

            Service.objects.create(
                start_time = start_at,
                end_time   = end_at,
                end_area   = end_point,
                fee        = total_fee,
                user       = user,
                kickboard  = kickboard,
            )

            return JsonResponse({'total_fee' : total_fee}, status = 201)
        
        except ValueError:
            return JsonResponse({'message' : 'DOES_NOT_MATCH_TIME_FORMAT'}, status = 400)
        
        except ArgumentError:
            return JsonResponse({'message' : 'TYPE_ERROR'}, status = 400)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
        except JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)
        
        except KickBoard.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_KICKBORD_NAME'}, status = 400)

