from django.urls import path
from .views import CollaborateurListCreateAPIView, CollaborateurRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('collaborateurs/', CollaborateurListCreateAPIView.as_view(), name='collaborateur-list-create'),
    path('collaborateurs/<int:pk>/', CollaborateurRetrieveUpdateDestroyAPIView.as_view(), name='collaborateur-retrieve-update-destroy'),
]
