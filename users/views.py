import json, jwt

from django.http   import JsonResponse
from django.views  import View

from users.models  import User
from deer.settings import SECRET_KEY, ALGORITHM

class SignInView(View):
  def post(self, request):
    try:
      data = json.loads(request.body)

      phone_number = data['phone_number']
      password     = data['password']

      if not User.objects.filter(phone_number = phone_number).exists():
        return JsonResponse({'message' : 'INVALID_PHONE_NUMBER'}, status = 401)

      user = User.objects.get(phone_number = phone_number)
      if not user.password == password:
        return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 401)

      access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
      return JsonResponse({'ACCESS_TOKEN' : access_token}, status = 200)

    except KeyError :
      return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)