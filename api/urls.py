from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'ConfigNumberCards', views.ConfigNumberCardsViewSet)
router.register(r'ConfigTimeBonus', views.ConfigTimeBonusViewSet)
router.register(r'SaveHighScores', views.SaveHighScoresViewSet)

urlpatterns = [
    path('', include(router.urls))
]