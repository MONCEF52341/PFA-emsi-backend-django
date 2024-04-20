#serializers.py sert à définir des sérialiseurs pour convertir les objets Django en formats de données comme JSON, et vice versa.

from rest_framework import serializers
from .models import *

class CollaborateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborateur
        fields = '__all__'

class DemandeAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeAbsence
        fields = '__all__'