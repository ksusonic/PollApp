from django.urls import path
from . import views

urlpatterns = [
    path('polls', views.ActivePollsViewSet.as_view(), name="Active polls"),
    # path('polls/<int:pk>', views.PollDetail.as_view(), name="Poll on id")
]
