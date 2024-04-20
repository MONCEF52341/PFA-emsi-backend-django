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

class EquipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class EquipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class EntiteJuridiqueListCreateAPIView(generics.ListCreateAPIView):
    queryset = EntiteJuridique.objects.all()
    serializer_class = EntiteJuridiqueSerializer

class EntiteJuridiqueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntiteJuridique.objects.all()
    serializer_class = EntiteJuridiqueSerializer

class LieuTravailListCreateAPIView(generics.ListCreateAPIView):
    queryset = LieuTravail.objects.all()
    serializer_class = LieuTravailSerializer

class LieuTravailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LieuTravail.objects.all()
    serializer_class = LieuTravailSerializer

class EmploiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emploi.objects.all()
    serializer_class = EmploiSerializer

class EmploiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emploi.objects.all()
    serializer_class = EmploiSerializer

class ContratListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

class ContratRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

class HeuresContractuellesListCreateAPIView(generics.ListCreateAPIView):
    queryset = HeuresContractuelles.objects.all()
    serializer_class = HeuresContractuellesSerializer

class HeuresContractuellesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeuresContractuelles.objects.all()
    serializer_class = HeuresContractuellesSerializer

class PolitiqueAbsencesListCreateAPIView(generics.ListCreateAPIView):
    queryset = PolitiqueAbsences.objects.all()
    serializer_class = PolitiqueAbsencesSerializer

class PolitiqueAbsencesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PolitiqueAbsences.objects.all()
    serializer_class = PolitiqueAbsencesSerializer

class CompteurAbsencesListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompteurAbsences.objects.all()
    serializer_class = CompteurAbsencesSerializer

class CompteurAbsencesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompteurAbsences.objects.all()
    serializer_class = CompteurAbsencesSerializer

class TypeAbsenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = TypeAbsence.objects.all()
    serializer_class = TypeAbsenceSerializer

class TypeAbsenceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeAbsence.objects.all()
    serializer_class = TypeAbsenceSerializer

class CycleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class CycleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class ConfigurationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class ConfigurationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class SeniorityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seniority.objects.all()
    serializer_class = SenioritySerializer

class SeniorityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seniority.objects.all()
    serializer_class = SenioritySerializer