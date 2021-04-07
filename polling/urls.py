from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('polls', views.ActivePolls)

urlpatterns = router.urls
