from django.urls import path
from .views import *

urlpatterns = [
    path('collaborateurs/', CollaborateurListCreateAPIView.as_view(), name='collaborateur-list-create'),
    path('collaborateurs/<int:pk>/', CollaborateurRetrieveUpdateDestroyAPIView.as_view(), name='collaborateur-retrieve-update-destroy'),
    path('demandeabsence/', DemandeAbsenceListCreateAPIView.as_view(), name='demandeabsence-list-create'),
    path('demandeabsence/<int:pk>/', DemandeAbsenceRetrieveUpdateDestroyAPIView.as_view(), name='demandeabsence-retrieve-update-destroy'),
    path('equipe/', EquipeListCreateAPIView.as_view(), name='equipe-list-create'),
    path('equipe/<int:pk>/', EquipeRetrieveUpdateDestroyAPIView.as_view(), name='equipe-retrieve-update-destroy'),
    path('entitejuridique/', EntiteJuridiqueListCreateAPIView.as_view(), name='entitejuridique-list-create'),
    path('entitejuridique/<int:pk>/', EntiteJuridiqueRetrieveUpdateDestroyAPIView.as_view(), name='entitejuridique-retrieve-update-destroy'),
    path('lieutravail/', LieuTravailListCreateAPIView.as_view(), name='lieutravail-list-create'),
    path('lieutravail/<int:pk>/', LieuTravailRetrieveUpdateDestroyAPIView.as_view(), name='lieutravail-retrieve-update-destroy'),
    path('emploi/', EmploiListCreateAPIView.as_view(), name='emploi-list-create'),
    path('emploi/<int:pk>/', EmploiRetrieveUpdateDestroyAPIView.as_view(), name='emploi-retrieve-update-destroy'),
    path('contrat/', ContratListCreateAPIView.as_view(), name='contrat-list-create'),
    path('contrat/<int:pk>/', ContratRetrieveUpdateDestroyAPIView.as_view(), name='contrat-retrieve-update-destroy'),
    path('heurescontractuelles/', HeuresContractuellesListCreateAPIView.as_view(), name='heurescontractuelles-list-create'),
    path('heurescontractuelles/<int:pk>/', HeuresContractuellesRetrieveUpdateDestroyAPIView.as_view(), name='heurescontractuelles-retrieve-update-destroy'),
    path('politiqueabsences/', PolitiqueAbsencesListCreateAPIView.as_view(), name='politiqueabsences-list-create'),
    path('politiqueabsences/<int:pk>/', PolitiqueAbsencesRetrieveUpdateDestroyAPIView.as_view(), name='politiqueabsences-retrieve-update-destroy'),
    path('compteurabsences/', CompteurAbsencesListCreateAPIView.as_view(), name='compteurabsences-list-create'),
    path('compteurabsences/<int:pk>/', CompteurAbsencesRetrieveUpdateDestroyAPIView.as_view(), name='compteurabsences-retrieve-update-destroy'),
    path('typeabsence/', TypeAbsenceListCreateAPIView.as_view(), name='typeabsence-list-create'),
    path('typeabsence/<int:pk>/', TypeAbsenceRetrieveUpdateDestroyAPIView.as_view(), name='typeabsence-retrieve-update-destroy'),
    path('cycle/', CycleListCreateAPIView.as_view(), name='cycle-list-create'),
    path('cycle/<int:pk>/', CycleRetrieveUpdateDestroyAPIView.as_view(), name='cycle-retrieve-update-destroy'),
    path('configuration/', ConfigurationListCreateAPIView.as_view(), name='configuration-list-create'),
    path('configuration/<int:pk>/', ConfigurationRetrieveUpdateDestroyAPIView.as_view(), name='configuration-retrieve-update-destroy'),
    path('seniority/', SeniorityListCreateAPIView.as_view(), name='seniority-list-create'),
    path('seniority/<int:pk>/', SeniorityRetrieveUpdateDestroyAPIView.as_view(), name='seniority-retrieve-update-destroy'),

]
