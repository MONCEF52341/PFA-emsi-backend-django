
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


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'


class EntiteJuridiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntiteJuridique
        fields = '__all__'


class LieuTravailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LieuTravail
        fields = '__all__'


class EmploiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emploi
        fields = '__all__'


class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'


class HeuresContractuellesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeuresContractuelles
        fields = '__all__'


class PolitiqueAbsencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolitiqueAbsences
        fields = '__all__'


class CompteurAbsencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteurAbsences
        fields = '__all__'


class TypeAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAbsence
        fields = '__all__'


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'


class SenioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Seniority
        fields = '__all__'
