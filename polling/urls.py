from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('polls', views.ActivePolls)
router.register('user', views.UserView)
router.register('vote', views.VoteView)


urlpatterns = router.urls
