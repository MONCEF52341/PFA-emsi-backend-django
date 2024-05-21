import random

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from rest_framework import generics

from .forms import *
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
    models = [Collaborateur, Configuration, TypeAbsence, CompteurAbsences, DemandeAbsence,
              PolitiqueAbsences, Contrat, Equipe, Emploi, HeuresContractuelles, EntiteJuridique,
              Cycle, Seniority, LieuTravail]  # Ajoutez tous vos modèles ici

    for model in models:
        count = model.objects.count()
        api_url = reverse(f'{model.__name__.lower()}-list-create')
        counts.append({'name': model._meta.verbose_name_plural, 'count': count, 'api_url': api_url})

    return render(request, 'dashboard.html', {'counts': counts})


@login_required
def accueil(request):
    return render(request, 'home.html')


def get_pris(employe):
    pris = 0
    demandes = DemandeAbsence.objects.filter(employe=employe)
    for demande in demandes:
        if demande.type_absence.deduire_du_compteur:
            if demande.date_fin:
                duree_abs = demande.date_fin - demande.date_debut
                pris += duree_abs.days
    return pris


def get_acquis(employe):
    return employe.politique_conges.compteur_absences.configuration.maximum_eligible_days


def get_demandes_absence(employe):
    return DemandeAbsence.objects.filter(employe=employe)


def create_demande_absence(request):
    if request.method == 'POST':
        form = DemandeAbsenceForm(request.POST)
        if form.is_valid():
            form.instance.employe = request.user.collaborateur
            form.initial.situation = "StandBy"
            form.save()
            return redirect(request.path)
    else:
        form = DemandeAbsenceForm()
    return form


@login_required
def dayoff(request):
    employe = request.user.collaborateur
    pris = get_pris(employe)
    acquis = get_acquis(employe)
    solde = acquis - pris
    demandes_absence = get_demandes_absence(employe)
    form = create_demande_absence(request)
    return render(request, 'dayoff/absence.html',
                  {'form': form, 'pris': pris, 'acquis': acquis, 'solde': solde, 'demandes_absence': demandes_absence})


@user_passes_test(lambda u: u.is_superuser)
def collaborateurs_list(request):
    ids_collaborateurs_archives = ArchiveCollaborateur.objects.values_list('id', flat=True)
    collaborateurs = Collaborateur.objects.exclude(id__in=ids_collaborateurs_archives)

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
            date_naissance=collaborateur.date_naissance,
            date_anciennete=collaborateur.date_anciennete,
            contrat=collaborateur.contrat,
            emploi=collaborateur.emploi,
            entite_juridique=collaborateur.entite_juridique,
            Equipe=collaborateur.Equipe,
            lieu_travail=collaborateur.lieu_travail,
            politique_conges=collaborateur.politique_conges,
            date_archivage=timezone.now()
        )
        # Supprimer le collaborateur
        collaborateur.delete()
        return redirect('liste_collaborateurs')
    return render(request, 'collaborateurs/supprimer_collaborateur.html', {'collaborateur': collaborateur})


@login_required
def equipes_list(request):
    query = request.GET.get('query')
    equipes = Equipe.objects.all()
    politiques_absences = PolitiqueAbsences.objects.all()
    if query:
        equipes = equipes.filter(nom__icontains=query)

    return render(request, 'equipes/equipe.html',
                  {'equipes': equipes, 'query': query, 'politiques_absences': politiques_absences})


@user_passes_test(lambda u: u.is_superuser)
def ajouter_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipes-list')
    else:
        form = EquipeForm()
    return render(request, 'equipes/ajouter_equipe.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def modifier_equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('equipes-list')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'equipes/modifier_equipe.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def supprimer_equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        equipe.delete()
        return redirect('liste_collaborateurs')
    return render(request, 'equipes/supprimer_equipe.html', {'equipe': equipe})


@login_required
def emplois_list(request):
    niveau = request.GET.get('niveau')
    query = request.GET.get('query')
    emplois = Emploi.objects.all()
    if query:
        emplois = emplois.filter(intitule__icontains=query)
    if niveau:
        emplois = emplois.filter(niveau=niveau)

    return render(request, 'emplois/emploi.html', {'emplois': emplois, 'niveau': niveau, 'query': query})


@user_passes_test(lambda u: u.is_superuser)
def ajouter_emploi(request):
    if request.method == 'POST':
        form = EmploiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplois-list')
    else:
        form = EmploiForm()
    return render(request, 'emplois/ajouter_emploi.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def modifier_emploi(request, pk):
    emploi = get_object_or_404(Emploi, pk=pk)
    if request.method == 'POST':
        form = EmploiForm(request.POST, instance=emploi)
        if form.is_valid():
            form.save()
            return redirect('emplois-list')
    else:
        form = EmploiForm(instance=emploi)
    return render(request, 'emplois/modifier_emploi.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def supprimer_emploi(request, pk):
    emploi = get_object_or_404(Emploi, pk=pk)
    if request.method == 'POST':
        emploi.delete()
        return redirect('emplois-list')
    return render(request, 'emplois/supprimer_emploi.html', {'emploi': emploi})


def appliquer_politique_absences(request):
    if request.method == 'POST':
        politique_id = request.POST.get('politique-absences')
        equipe_id = request.POST.get('equipe-id')

        # Récupérer l'équipe
        equipe = Equipe.objects.get(pk=equipe_id)

        # Assigner la politique d'absences à l'équipe
        politique_absences = PolitiqueAbsences.objects.get(pk=politique_id)

        # Appliquer la politique d'absences à tous les employés de l'équipe
        employes = Collaborateur.objects.filter(equipe=equipe)
        for employe in employes:
            employe.politique_absences = politique_absences
            employe.save()

        return redirect('equipes-list')
    else:
        politiques_absences = PolitiqueAbsences.objects.all()
        return render(request, 'popup-form.html', {'politiques_absences': politiques_absences})


def create_organization_chart(collaborateur):
    ids_collaborateurs_archives = ArchiveCollaborateur.objects.values_list('id', flat=True)
    chart = {'collaborateur': collaborateur, 'subordinates': []}
    subordinates = Collaborateur.objects.filter(manager=collaborateur).exclude(id__in=ids_collaborateurs_archives)

    for subordinate in subordinates:
        chart['subordinates'].append(create_organization_chart(subordinate))

    return chart


def organization_chart(request):
    ids_collaborateurs_archives = ArchiveCollaborateur.objects.values_list('id', flat=True)
    top_level_collaborateurs = Collaborateur.objects.filter(manager=None).exclude(id__in=ids_collaborateurs_archives)

    org_charts = []
    for collaborateur in top_level_collaborateurs:
        org_charts.append(create_organization_chart(collaborateur))

    return render(request, 'organization_chart.html', {'org_charts': org_charts})


@login_required
def mon_profil(request):
    collaborateur = request.user.collaborateur  # Récupérer le profil du collaborateur actuellement connecté
    if request.method == 'POST':
        form = MyprofileForm(request.POST, instance=collaborateur)
        if form.is_valid():
            form.save()
            return redirect('mon_profil')
    else:
        form = MyprofileForm(instance=collaborateur)

    return render(request, 'myprofile.html', {'form': form})


def populate_database(request):
    if request.method == 'POST':
        form = PopulateDatabaseForm(request.POST)
        if form.is_valid():
            number_of_entries = form.cleaned_data['number_of_entries']
            fake = Faker()
            for _ in range(number_of_entries):
                # Créez une instance de votre modèle avec des données fictives
                # Assurez-vous d'importer votre modèle et de remplacer "VotreModele" par le nom de votre modèle
                instance = Collaborateur(
                    prenom=fake.first_name(),
                    nom=fake.last_name(),
                    avatar=None,  # Si vous ne générez pas d'avatar fictif
                    matricule=fake.unique.random_number(digits=11),
                    date_naissance=fake.date_of_birth(minimum_age=18, maximum_age=90),
                    genre=random.choice(['M', 'F']),
                    nationalite=fake.country(),
                    numero_telephone=''.join(filter(str.isdigit, fake.phone_number())),
                    adresse=fake.street_address(),
                    ville=fake.city(),
                    code_postal=fake.postcode(),
                    departement=fake.state(),
                    pays=fake.country(),
                    contact_urgence_nom=fake.name(),
                    contact_urgence_telephone=fake.phone_number(),
                    email_personnel=fake.email(),
                    email_professionnel=fake.company_email(),
                    entite_juridique=EntiteJuridique.objects.order_by('?').first(),
                    # Choisissez une entité juridique aléatoire
                    date_anciennete=fake.date_this_decade(),
                    lieu_travail=LieuTravail.objects.order_by('?').first(),  # Choisissez un lieu de travail aléatoire
                    politique_conges=PolitiqueAbsences.objects.order_by('?').first(),
                    # Choisissez une politique de congés aléatoire
                    Equipe=Equipe.objects.order_by('?').first(),  # Choisissez une équipe aléatoire
                    contrat=Contrat.objects.order_by('?').first(),  # Choisissez un contrat aléatoire
                    emploi=Emploi.objects.order_by('?').first(),  # Choisissez un emploi aléatoire
                    manager=Collaborateur.objects.order_by('?').last(),  # Choisissez un manager aléatoire
                )
                instance.save()
            return render(request,
                          'myprofile.html')  # Redirigez vers une page de succès ou affichez un message de succès
    else:
        form = PopulateDatabaseForm()
    return render(request, 'populate.html', {'form': form})


def vider(request):
    if request.method == 'POST':
        ArchiveCollaborateur.objects.all().delete()
        return render(request, 'myprofile.html')  # Redirigez vers une page de succès ou affichez un message de succès
    return render(request, 'purge.html')


def calendar_Absences(request):
    evenements = DemandeAbsence.objects.all()
    events_data = []
    for evenement in evenements:
        events_data.append({
            'title': f"{evenement.employe.nom} {evenement.employe.prenom}, {evenement.type_absence.nom}, {evenement.date_debut.strftime('%Y-%m-%d')}" + (
                f" - {evenement.date_fin.strftime('%Y-%m-%d')}" if evenement.date_fin else ""),
            'start': evenement.date_debut.strftime('%Y-%m-%d'),
            'end': evenement.date_fin.strftime('%Y-%m-%d') if evenement.date_fin else "",
        })
    return JsonResponse(events_data, safe=False)
