from django.urls import path
from .views import ActivePollsViewSet, PollDetail

urlpatterns = [
    path('polls', ActivePollsViewSet.as_view(), name="Active polls"),
    path('polls/<int:pk>', PollDetail.as_view(), name="Poll on id")

]
