import jwt, json

from django.test             import TestCase, Client
from django.contrib.gis.geos import Polygon, Point, MultiPoint

from users.models            import User
from services.models         import *
from deer.settings           import SECRET_KEY, ALGORITHM

class CalculateTest(TestCase):
    def setUp(self):
        global headers
        access_token  = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        headers       = {'HTTP_AUTHORIZATION': access_token}

        User.objects.create(
            id           = 1,
            phone_number = "010-1111-1111",
            password     = "1111"
        )
        
        Area.objects.create(
            id            = 1,
            area_center   = Point((37.55339275142622, 127.0739886462907)),
            area_boundary = Polygon(((37.559260, 127.073697), (37.549197, 127.068847), (37.548049, 127.074528), (37.556847, 127.079042), (37.559260, 127.073697))),
            area_coords   = MultiPoint(Point(37.559260, 127.073697), Point(37.549197, 127.068847), Point(37.548049, 127.074528), Point(37.556847, 127.079042)),
            basic_fee     = 1000,
            minute_fee    = 200
        )
        
        ForbiddenArea.objects.create(
            id                 = 1,
            area_id            = 1, 
            forbidden_boundary = Polygon(((37.552644, 127.073592), (37.552134, 127.072820), (37.550611, 127.074515), (37.551391, 127.075596), (37.552644, 127.073592))),
            forbidden_coords   = MultiPoint(Point(37.552644, 127.073592), Point(37.552134, 127.072820), Point(37.550611, 127.074515), Point(37.551391, 127.075596))
        )
        
        ParkingZone.objects.create(
            id             = 1,
            area_id        = 1, 
            parking_center = Point((37.555222, 127.075695)), 
            parking_radius = 30
        )

        KickBoard.objects.create(
            id      = 1, 
            name    = '썬더볼트', 
            area_id = 1
        )

    def tearDown(self):
        User.objects.all().delete()
        Area.objects.all().delete()
        ForbiddenArea.objects.all().delete()
        ParkingZone.objects.all().delete()
        KickBoard.objects.all().delete()

    def test_post_success_calculate(self):
        client = Client()
        data   = {
            "kickboard_name" : "썬더볼트",
            "end_lat"        : 37.556251,
            "end_lng"        : 127.074597,
            "start_at"       : "2021-11-20 10:20:00",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
            {
                'total_fee' : 6000
            }
        )

    def test_post_failure_value_error(self):
        client = Client()
        data   = {
            "kickboard_name" : "썬더볼트",
            "end_lat"        : 37.556251,
            "end_lng"        : 127.074597,
            "start_at"       : "123",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'message' : 'DOES_NOT_MATCH_TIME_FORMAT'
            }
        )
    
    def test_post_failure_type_error(self):
        client = Client()
        data   = {
            "kickboard_name" : "썬더볼트",
            "end_lat"        : 'abc',
            "end_lng"        : 127.074597,
            "start_at"       : "2021-11-20 10:20:00",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'message' : 'TYPE_ERROR'
            }
        )

    def test_post_failure_key_error(self):
        client = Client()
        data   = {
            "kickboard_name" : "썬더볼트",
            "start_at"       : "2021-11-20 10:20:00",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'message' : 'KEY_ERROR'
            }
        )

    def test_post_failure_invalid_kickboard_name(self):
        client = Client()
        data   = {
            "kickboard_name" : "씽씽이",
            "end_lat"        : 37.556251,
            "end_lng"        : 127.074597,
            "start_at"       : "2021-11-20 10:20:00",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'message' : 'INVALID_KICKBORD_NAME'
            }
        )

    def test_post_failure_invalid_token(self):
        client = Client()
        data   = {
            "kickboard_name" : "뿡뿡이",
            "end_lat"        : 37.556251,
            "end_lng"        : 127.074597,
            "start_at"       : "2021-11-20 10:20:00",
            "end_at"         : "2021-11-20 10:50:00"
        }

        response = client.post('/services/settlement', json.dumps(data), content_type = 'applications/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), 
            {
                'message' : 'INVALID_TOKEN'
            }
        )
