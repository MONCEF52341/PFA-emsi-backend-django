from rest_framework import generics
from .models import *
from .serializers import *

class CollaborateurListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collaborateur.objects.all()
    serializer_class = CollaborateurSerializer

class CollaborateurRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaborateur.objects.all()
    serializer_class = CollaborateurSerializer

class DemandeAbsenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = DemandeAbsence.objects.all()
    serializer_class = DemandeAbsenceSerializer

class DemandeAbsenceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandeAbsence.objects.all()
    serializer_class = DemandeAbsenceSerializer