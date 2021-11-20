from django.urls    import path
from services.views import CalculateView

urlpatterns = [
    path('/settlement', CalculateView.as_view()),
]