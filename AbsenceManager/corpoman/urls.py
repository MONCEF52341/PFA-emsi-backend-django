from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/collaborateurs/', CollaborateurListCreateAPIView.as_view(), name='collaborateur-list-create'),
    path('api/collaborateurs/<int:pk>/', CollaborateurRetrieveUpdateDestroyAPIView.as_view(),
         name='collaborateur-retrieve-update-destroy'),
    path('api/demandeabsence/', DemandeAbsenceListCreateAPIView.as_view(), name='demandeabsence-list-create'),
    path('api/demandeabsence/<int:pk>/', DemandeAbsenceRetrieveUpdateDestroyAPIView.as_view(),
         name='demandeabsence-retrieve-update-destroy'),
    path('api/equipe/', EquipeListCreateAPIView.as_view(), name='equipe-list-create'),
    path('api/equipe/<int:pk>/', EquipeRetrieveUpdateDestroyAPIView.as_view(), name='equipe-retrieve-update-destroy'),
    path('api/entitejuridique/', EntiteJuridiqueListCreateAPIView.as_view(), name='entitejuridique-list-create'),
    path('api/entitejuridique/<int:pk>/', EntiteJuridiqueRetrieveUpdateDestroyAPIView.as_view(),
         name='entitejuridique-retrieve-update-destroy'),
    path('api/lieutravail/', LieuTravailListCreateAPIView.as_view(), name='lieutravail-list-create'),
    path('api/lieutravail/<int:pk>/', LieuTravailRetrieveUpdateDestroyAPIView.as_view(),
         name='lieutravail-retrieve-update-destroy'),
    path('api/emploi/', EmploiListCreateAPIView.as_view(), name='emploi-list-create'),
    path('api/emploi/<int:pk>/', EmploiRetrieveUpdateDestroyAPIView.as_view(), name='emploi-retrieve-update-destroy'),
    path('api/contrat/', ContratListCreateAPIView.as_view(), name='contrat-list-create'),
    path('api/contrat/<int:pk>/', ContratRetrieveUpdateDestroyAPIView.as_view(),
         name='contrat-retrieve-update-destroy'),
    path('api/heurescontractuelles/', HeuresContractuellesListCreateAPIView.as_view(),
         name='heurescontractuelles-list-create'),
    path('api/heurescontractuelles/<int:pk>/', HeuresContractuellesRetrieveUpdateDestroyAPIView.as_view(),
         name='heurescontractuelles-retrieve-update-destroy'),
    path('api/politiqueabsences/', PolitiqueAbsencesListCreateAPIView.as_view(), name='politiqueabsences-list-create'),
    path('api/politiqueabsences/<int:pk>/', PolitiqueAbsencesRetrieveUpdateDestroyAPIView.as_view(),
         name='politiqueabsences-retrieve-update-destroy'),
    path('api/compteurabsences/', CompteurAbsencesListCreateAPIView.as_view(), name='compteurabsences-list-create'),
    path('api/compteurabsences/<int:pk>/', CompteurAbsencesRetrieveUpdateDestroyAPIView.as_view(),
         name='compteurabsences-retrieve-update-destroy'),
    path('api/typeabsence/', TypeAbsenceListCreateAPIView.as_view(), name='typeabsence-list-create'),
    path('api/typeabsence/<int:pk>/', TypeAbsenceRetrieveUpdateDestroyAPIView.as_view(),
         name='typeabsence-retrieve-update-destroy'),
    path('api/cycle/', CycleListCreateAPIView.as_view(), name='cycle-list-create'),
    path('api/cycle/<int:pk>/', CycleRetrieveUpdateDestroyAPIView.as_view(), name='cycle-retrieve-update-destroy'),
    path('api/configuration/', ConfigurationListCreateAPIView.as_view(), name='configuration-list-create'),
    path('api/configuration/<int:pk>/', ConfigurationRetrieveUpdateDestroyAPIView.as_view(),
         name='configuration-retrieve-update-destroy'),
    path('api/seniority/', SeniorityListCreateAPIView.as_view(), name='seniority-list-create'),
    path('api/seniority/<int:pk>/', SeniorityRetrieveUpdateDestroyAPIView.as_view(),
         name='seniority-retrieve-update-destroy'),
    path('dashboard/', dashboard, name='dashboard'),
    path('home/', accueil, name='accueil'),

    path('collaborateurs/', collaborateurs_list, name='liste_collaborateurs'),
    path('ajouter-collaborateur/', ajouter_collaborateur, name='ajouter_collaborateur'),
    path('modifier-collaborateur/<int:pk>/', modifier_collaborateur, name='modifier_collaborateur'),
    path('supprimer-collaborateur/<int:pk>/', supprimer_collaborateur, name='supprimer_collaborateur'),

    path('equipes/', equipes_list, name='equipes-list'),
    path('ajouter-equipe/', ajouter_equipe, name='ajouter_equipe'),
    path('modifier-equipe/<int:pk>/', modifier_equipe, name='modifier_equipe'),
    path('supprimer-equipe/<int:pk>/', supprimer_equipe, name='supprimer_equipe'),

    path('emplois/', emplois_list, name='emploi-list'),
    path('ajouter-emploi/', ajouter_emploi, name='ajouter_emploi'),
    path('modifier-emploi/<int:pk>/', modifier_emploi, name='modifier_emploi'),
    path('supprimer-emploi/<int:pk>/', supprimer_emploi, name='supprimer_emploi'),

    path('dayoff/', dayoff, name='dayoff'),
    path('changer_situation_absence/<int:pk>/<str:situation>/', changer_situation_absence, name='changer_situation_absence'),

    path('appliquer-politique-absences/', appliquer_politique_absences, name='appliquer_politique_absences'),
    path('mon-profil/', mon_profil, name='mon_profil'),
    path('organigramme/', organization_chart, name='organigramme'),
    path('populate/', populate_database, name='populate'),
    path('evenements', calendar_Absences, name='evenements'),
    path('absmanagement/', absmanagement, name='absmanagement'),
    path('myabs', myabs, name='myabs'),
    path('purge/', vider, name='vider_archive_collaborateur')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)