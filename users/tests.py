import jwt, json

from django.test   import TestCase, Client

from users.models  import User
from deer.settings import SECRET_KEY, ALGORITHM

class SignInTest(TestCase):
  def setUp(self):
    User.objects.create(
        id           = 1,
        phone_number = "010-1111-1111",
        password     = "1111"
    )

  def tearDown(self):
    User.objects.all().delete()

  def test_post_success_signin(self):
    client = Client()
    user   = {
      "phone_number" : "010-1111-1111",
      "password"     : "1111"
    }
    response = client.post('/users/signin', json.dumps(user), content_type = 'applications/json')
    user     = User.objects.get(phone_number = user['phone_number'])

    access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

    self.assertEqual(response.json(), {'ACCESS_TOKEN' : access_token})
    self.assertEqual(response.status_code, 200)

  def test_post_failure_signin_invalid_phone_number(self):
    client = Client()
    user   = {
      "phone_number" : "010-일일일일-일일일일",
      "password"     : "1111"
    }
    response = client.post('/users/signin', json.dumps(user), content_type = 'applications/json')

    self.assertEqual(response.json(), {'message' : 'INVALID_PHONE_NUMBER'})
    self.assertEqual(response.status_code, 401)

  def test_post_failure_signin_invalid_password(self):
    client = Client()

    user = {
      "phone_number" : "010-1111-1111",
      "password"     : "일일일일"
    }

    response = client.post('/users/signin', json.dumps(user), content_type = 'applications/json')

    self.assertEqual(response.json(),{'message' : 'INVALID_PASSWORD'})
    self.assertEqual(response.status_code, 401)

  def test_signin_failure_key_error(self):
    client = Client()

    user = {
      "password" : "1111"
    }

    response = client.post('/users/signin', json.dumps(user), content_type = 'application/json')

    self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
    self.assertEqual(response.status_code, 400)