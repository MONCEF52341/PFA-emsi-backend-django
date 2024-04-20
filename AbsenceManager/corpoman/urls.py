from django.urls import path
from .views import *

urlpatterns = [
    path('collaborateurs/', CollaborateurListCreateAPIView.as_view(), name='collaborateur-list-create'),
    path('collaborateurs/<int:pk>/', CollaborateurRetrieveUpdateDestroyAPIView.as_view(), name='collaborateur-retrieve-update-destroy'),
    path('demandeabsence/', DemandeAbsenceListCreateAPIView.as_view(), name='demandeabsence-list-create'),
    path('demandeabsence/<int:pk>/', DemandeAbsenceRetrieveUpdateDestroyAPIView.as_view(), name='demandeabsence-retrieve-update-destroy'),
    
]
