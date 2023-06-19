from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.
class ConfigNumberCardsViewSet(viewsets.ModelViewSet):
    queryset = ConfigNumberCards.objects.all()
    serializer_class = ConfigNumberCardsSerializer

class ConfigTimeBonusViewSet(viewsets.ModelViewSet):
    queryset = ConfigTimeBonus.objects.all()
    serializer_class = ConfigTimeBonusSerializer

class SaveHighScoresViewSet(viewsets.ModelViewSet):
    queryset = SaveHighScores.objects.all()
    serializer_class = SaveHighScoresSerializer
    