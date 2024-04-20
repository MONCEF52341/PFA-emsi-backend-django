from rest_framework import serializers
from .models import Collaborateur

class CollaborateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborateur
        fields = '__all__'
