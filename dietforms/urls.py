from django.urls import path
from .views import get_diet_plan

urlpatterns = [
    path('', get_diet_plan, name='get-diet-plan'),
]