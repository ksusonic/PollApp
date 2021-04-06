from django.urls import path
from .views import Polls

urlpatterns = [
    path('', Polls.as_view(), name='quiz'),
]
