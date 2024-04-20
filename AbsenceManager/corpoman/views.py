from rest_framework import generics
from .models import Collaborateur
from .serializers import CollaborateurSerializer

class CollaborateurListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collaborateur.objects.all()
    serializer_class = CollaborateurSerializer

class CollaborateurRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaborateur.objects.all()
    serializer_class = CollaborateurSerializer
