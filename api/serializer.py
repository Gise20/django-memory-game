from rest_framework import serializers
from .models import *

class ConfigNumberCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigNumberCards
        fields = ('Easy','Medium','Hard')

class ConfigTimeBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigTimeBonus
        fields = ('Easy','Medium','Hard')

class SaveHighScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveHighScores
        fields = ('__all__')