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

class equipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class entitejuridiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntiteJuridique
        fields = '__all__'

class lieutravailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LieuTravail
        fields = '__all__'

class emploiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emploi
        fields = '__all__'

class contratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'

class heurescontractuellesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeuresContractuelles
        fields = '__all__'

class politiqueabsencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolitiqueAbsences
        fields = '__all__'

class compteurabsencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteurAbsences
        fields = '__all__'

class typeabsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAbsence
        fields = '__all__'

class cycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'

class configurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class senioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Seniority
        fields = '__all__'