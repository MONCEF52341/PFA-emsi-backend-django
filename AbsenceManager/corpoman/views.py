from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required,user_passes_test
from rest_framework import generics
from .forms import *
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

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    counts = []
    models = [Collaborateur,Configuration,TypeAbsence,CompteurAbsences,DemandeAbsence,
              PolitiqueAbsences,Contrat,Equipe,Emploi,HeuresContractuelles,EntiteJuridique,
              Cycle,Seniority,LieuTravail]  # Ajoutez tous vos modèles ici

    for model in models:
        count = model.objects.count()
        api_url = reverse(f'{model.__name__.lower()}-list-create')
        counts.append({'name': model._meta.verbose_name_plural, 'count': count, 'api_url': api_url})

    return render(request, 'dashboard.html', {'counts': counts})

@login_required
def accueil(request):
    return render(request, 'home.html')


@user_passes_test(lambda u: u.is_superuser)
def collaborateurs_list(request):
    collaborateurs = Collaborateur.objects.all()

    # Récupérer le paramètre de tri de l'URL
    sort_by = request.GET.get('sort')

    # Récupérer l'état de tri actuel de la session
    sort_order = request.session.get('sort_order', 'asc')

    # Basculer entre l'ordre ascendant et descendant si le même en-tête est cliqué à nouveau
    if sort_by == request.session.get('sort_by') and sort_order == 'asc':
        sort_order = 'desc'
    else:
        sort_order = 'asc'

    # Enregistrer le nouvel état de tri dans la session
    request.session['sort_by'] = sort_by
    request.session['sort_order'] = sort_order

    # Trier les collaborateurs en fonction du paramètre de tri et de l'ordre
    if sort_by == 'nom':
        collaborateurs = collaborateurs.order_by('-nom' if sort_order == 'desc' else 'nom')
    elif sort_by == 'prenom':
        collaborateurs = collaborateurs.order_by('-prenom' if sort_order == 'desc' else 'prenom')
    elif sort_by == 'emploi':
        collaborateurs = collaborateurs.order_by('-emploi' if sort_order == 'desc' else 'emploi')
    elif sort_by == 'date_anciennete':
        collaborateurs = collaborateurs.order_by('-date_anciennete' if sort_order == 'desc' else 'date_anciennete')

    return render(request, 'collaborateurs/collaborateurs.html', {'collaborateurs': collaborateurs})

@user_passes_test(lambda u: u.is_superuser)
def ajouter_collaborateur(request):
    if request.method == 'POST':
        form = CollaborateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_collaborateurs')
    else:
        form = CollaborateurForm()
    return render(request, 'collaborateurs/ajouter_collaborateur.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def modifier_collaborateur(request, pk):
    collaborateur = get_object_or_404(Collaborateur, pk=pk)
    if request.method == 'POST':
        form = CollaborateurForm(request.POST, instance=collaborateur)
        if form.is_valid():
            form.save()
            return redirect('liste_collaborateurs')
    else:
        form = CollaborateurForm(instance=collaborateur)
    return render(request, 'collaborateurs/modifier_collaborateur.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def supprimer_collaborateur(request, pk):
    collaborateur = get_object_or_404(Collaborateur, pk=pk)
    if request.method == 'POST':
        # Créer une instance de ArchiveCollaborateur et y copier les données du collaborateur
        archive_collaborateur = ArchiveCollaborateur.objects.create(
            prenom=collaborateur.prenom,
            nom=collaborateur.nom,
            # Copier les autres champs au besoin
            date_archivage=timezone.now()
        )
        # Supprimer le collaborateur
        collaborateur.delete()
        return redirect('liste_collaborateurs')
    return render(request, 'collaborateurs/supprimer_collaborateur.html', {'collaborateur': collaborateur})

@user_passes_test(lambda u: u.is_superuser)
def detail_collaborateur(request, pk):
    collaborateur = get_object_or_404(Collaborateur, pk=pk)
    return render(request, 'collaborateurs/detail_collaborateur.html', {'collaborateur': collaborateur})

def dayoff(request):
    return render(request, 'dayoff/absence.html')