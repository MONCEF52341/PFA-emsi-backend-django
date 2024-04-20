from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Collaborateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    matricule = models.CharField(max_length=100, verbose_name="Matricule")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    GENRE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name="Genre")
    nationalite = models.CharField(max_length=100, verbose_name="Nationalité")
    numero_telephone = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    adresse = models.CharField(max_length=255, verbose_name="Adresse")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    code_postal = models.CharField(max_length=20, verbose_name="Code postal")
    departement = models.CharField(max_length=100, verbose_name="Département")
    pays = models.CharField(max_length=100, verbose_name="Pays")
    contact_urgence_nom = models.CharField(max_length=100,
                                           verbose_name="Nom de la personne à contacter en cas d'urgence")
    contact_urgence_telephone = models.CharField(max_length=20,
                                                 verbose_name="Téléphone de la personne à contacter en cas d'urgence")
    email_personnel = models.EmailField(verbose_name="Email Personnel")
    email_professionnel = models.EmailField(verbose_name="Email Professionnel")
    entite_juridique = models.ForeignKey('EntiteJuridique', on_delete=models.CASCADE,
                                         verbose_name="Entité Juridique associée à l'employé")
    date_anciennete = models.DateField(verbose_name="Date d'ancienneté")
    lieu_travail = models.ForeignKey('LieuTravail', on_delete=models.CASCADE, verbose_name="Lieu de travail")
    politique_conges = models.ForeignKey('PolitiqueAbsences', on_delete=models.CASCADE,
                                         verbose_name="Politique de congés")
    Equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, verbose_name="Équipe")
    contrat = models.ForeignKey('Contrat', on_delete=models.CASCADE, verbose_name="Contrat")
    emploi = models.ForeignKey('Emploi', on_delete=models.CASCADE, verbose_name="Emploi")
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Manager")

    class Meta:
        verbose_name = "Collaborateur"
        verbose_name_plural = "Collaborateurs"

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"


class DemandeAbsence(models.Model):
    employe = models.ForeignKey('Collaborateur', on_delete=models.CASCADE, verbose_name="Employé")
    approbateur = models.ForeignKey('Collaborateur', on_delete=models.SET_NULL, null=True, blank=True, related_name="approbateur", verbose_name="Approbateur")
    type_absence = models.ForeignKey('TypeAbsence', on_delete=models.CASCADE, verbose_name="Type d'absence")
    description = models.TextField(verbose_name="Description")
    date_debut = models.DateField(verbose_name="Date début")
    date_fin = models.DateField(null=True, blank=True, verbose_name="Date fin")
    documents = models.FileField(upload_to="documents_joints", verbose_name="Documents joints", null=True, blank=True)

    class Meta:
        verbose_name = "Demande d'absence"
        verbose_name_plural = "Demandes d'absence"

    def __str__(self):
        if self.date_fin:
            return f"Demande d'absence pour {self.employe} du {self.date_debut} au {self.date_fin}"
        else:
            return f"Demande d'absence pour {self.employe} à partir du {self.date_debut}"

class Equipe(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    responsable = models.ForeignKey('Collaborateur', on_delete=models.CASCADE, verbose_name="Manager/Responsable")

    class Meta:
        verbose_name = "Équipe"
        verbose_name_plural = "Équipes"

    def __str__(self):
        return self.nom


class EntiteJuridique(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    raison_sociale = models.CharField(max_length=255, verbose_name="Raison sociale (Nom)")
    matricule = models.CharField(max_length=100, verbose_name="Matricule")
    adresse_domiciliation = models.CharField(max_length=255, verbose_name="Adresse de Domiciliation")
    ville = models.CharField(max_length=100, verbose_name="Ville")
    code_postal = models.CharField(max_length=20, verbose_name="Code postal")
    departement = models.CharField(max_length=100, verbose_name="Département")
    pays = models.CharField(max_length=100, verbose_name="Pays")

    class Meta:
        verbose_name = "Entité Juridique"
        verbose_name_plural = "Entités Juridiques"

    def __str__(self):
        return self.id


class LieuTravail(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    TYPE_CHOICES = (
        ('OpenSpace', 'OpenSpace'),
        ('BureauPropre', 'Bureau Propre'),
        ('Itinerant', 'Itinérant'),
        ('Hybride', 'Hybride'),
    )

    designation = models.CharField(max_length=255, verbose_name="Désignation")
    description = models.TextField(verbose_name="Description")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type")
    capacite = models.PositiveIntegerField(verbose_name="Capacité")

    class Meta:
        verbose_name = "Lieu de travail"
        verbose_name_plural = "Lieux de travail"

    def __str__(self):
        return self.id


class Emploi(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    INTITULE_CHOICES = (
        ('Junior', 'Junior'),
        ('Moyen', 'Moyen'),
        ('Senior', 'Senior'),
    )

    intitule = models.CharField(max_length=255, verbose_name="Intitulé de poste")
    entite_juridique = models.ForeignKey(
        'EntiteJuridique',
        on_delete=models.CASCADE,
        verbose_name="Entité Juridique"
    )
    niveau = models.CharField(
        max_length=10,
        choices=INTITULE_CHOICES,
        verbose_name="Niveau"
    )

    class Meta:
        verbose_name = "Emploi"
        verbose_name_plural = "Emplois"

    def __str__(self):
        return self.id


class Contrat(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    emploi_concerne = models.ForeignKey(
        'Emploi',
        on_delete=models.CASCADE,
        verbose_name="Emploi concerné"
    )
    date_entree_vigueur = models.DateField(verbose_name="Date d'entrée en vigueur du contrat")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    periode_dessai = models.BooleanField(verbose_name="Période d'essai")

    heures_contractuelles = models.ForeignKey(
        'HeuresContractuelles',
        on_delete=models.CASCADE,
        verbose_name="Heures contractuelles"
    )

    class Meta:
        verbose_name = "Contrat"
        verbose_name_plural = "Contrats"

    def __str__(self):
        return self.id


class HeuresContractuelles(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    heures_par_jour = models.PositiveIntegerField(verbose_name="Heures par jour")
    lundi = models.BooleanField(default=True)
    mardi = models.BooleanField(default=True)
    mercredi = models.BooleanField(default=True)
    jeudi = models.BooleanField(default=True)
    vendredi = models.BooleanField(default=True)
    samedi = models.BooleanField(default=False)
    dimanche = models.BooleanField(default=False)
    max_heures_par_semaine = models.PositiveIntegerField(verbose_name="Nombre maximum d'heures par semaine")
    max_heures_par_an = models.PositiveIntegerField(verbose_name="Nombre maximum d'heures par an")

    class Meta:
        verbose_name = "Heures contractuelles"
        verbose_name_plural = "Heures contractuelles"

    def __str__(self):
        return self.id


class PolitiqueAbsences(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    compteur_absences = models.ForeignKey(
        'CompteurAbsences',
        on_delete=models.CASCADE,
        verbose_name="Compteur d'absences"
    )

    class Meta:
        verbose_name = "Politique d'absences"
        verbose_name_plural = "Politiques d'absences"

    def __str__(self):
        return self.id


class CompteurAbsences(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    NOM_CHOICES = (
        ('solde_fixe', 'Solde fixe'),
        ('heures_supplementaires', 'Heures supplémentaires'),
        ('sur_base_heures_travaillees', 'Sur la base des heures travaillées'),
    )

    nom = models.CharField(max_length=100, verbose_name="Nom")
    type_compteur = models.CharField(
        max_length=50,
        choices=NOM_CHOICES,
        verbose_name="Type de compteur"
    )
    types_absences_autorises = models.ManyToManyField(
        'TypeAbsence',
        verbose_name="Liste de types d'absences autorisés"
    )
    cycle = models.ForeignKey(
        'Cycle',
        on_delete=models.CASCADE,
        verbose_name="Cycle"
    )
    configuration = models.ForeignKey(
        'Configuration',
        on_delete=models.CASCADE,
        verbose_name="Configuration"
    )

    class Meta:
        verbose_name = "Compteur d'absences"
        verbose_name_plural = "Compteurs d'absences"

    def __str__(self):
        return self.id


class TypeAbsence(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    deduire_du_compteur = models.BooleanField(verbose_name="Déduire ce temps depuis le compteur")
    absence_remuneree = models.BooleanField(verbose_name="Absences rémunérée")
    date_fin_obligatoire = models.BooleanField(verbose_name="Date de fin obligatoire")
    demander_absence = models.BooleanField(verbose_name="Permettre de demander ce type d'absences")
    autoriser_pieces_jointes = models.BooleanField(verbose_name="Autoriser les pièces jointes")
    pieces_jointes_obligatoires = models.BooleanField(verbose_name="Obliger les pièces jointes")
    description_obligatoire = models.BooleanField(verbose_name="Description obligatoire")
    approbation_automatique = models.BooleanField(verbose_name="Approbation Automatique")

    class Meta:
        verbose_name = "Type d'absence"
        verbose_name_plural = "Types d'absences"

    def __str__(self):
        return self.id


class Cycle(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    MOIS_CHOICES = (
        ('janvier', 'Janvier'),
        ('février', 'Février'),
        ('mars', 'Mars'),
        ('avril', 'Avril'),
        ('mai', 'Mai'),
        ('juin', 'Juin'),
        ('juillet', 'Juillet'),
        ('août', 'Août'),
        ('septembre', 'Septembre'),
        ('octobre', 'Octobre'),
        ('novembre', 'Novembre'),
        ('décembre', 'Décembre'),
        ('debut_contrat', 'Début du contrat'),
    )

    DUREE_CHOICES = (
        (1, '1 mois'),
        (2, '2 mois'),
        (3, '3 mois'),
        (6, '6 mois'),
        (12, '12 mois'),
    )

    mois_debut = models.CharField(
        max_length=20,
        choices=MOIS_CHOICES,
        verbose_name="Mois de début"
    )
    duree = models.IntegerField(
        choices=DUREE_CHOICES,
        verbose_name="Durée (en mois)"
    )

    class Meta:
        verbose_name = "Cycle"
        verbose_name_plural = "Cycles"

    def __str__(self):
        return self.id


class Configuration(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    # Paramètres du compteur d'absences
    maximum_eligible_days = models.PositiveIntegerField(
        verbose_name="Nombre maximum de jours éligibles"
    )
    MODE_CHOICES = (
        ('cumul', 'Cumul'),
        ('reset', 'Reset')
    )
    accumulation_mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES,
        verbose_name="Mode d'accumulation des jours d'absences"
    )
    absence_day_use = models.CharField(
        max_length=100,
        verbose_name="Utilisation des jours d'absences"
    )
    negative_balance = models.BooleanField(
        verbose_name="Autorisation de solde négatif"
    )
    nombre_jours_reportes = models.PositiveIntegerField(
        verbose_name="Nombre de jours pouvant être reportés",
        null=True,
        blank=True
    )
    number_of_reported_days = models.PositiveIntegerField(
        verbose_name="Date d'expiration des jours reportés (en mois)",
        validators=[MinValueValidator(1), MaxValueValidator(60)],
        null=True,
        blank=True
    )
    seniority = models.ForeignKey(
        'Seniority',
        on_delete=models.CASCADE,
        verbose_name="Période d'ancienneté"
    )

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return self.id


class Seniority(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    # Ancienneté requise du collaborateur (en mois) entre 1 et 60
    seniority_required = models.IntegerField(
        verbose_name=("Ancienneté requise du collaborateur (en mois)"),
        help_text=("Veuillez entrer l'ancienneté requise du collaborateur en mois (entre 1 et 60)."),
        validators=[MinValueValidator(1), MaxValueValidator(60)],
        unique=True
    )

    # Jours de congé supplémentaire
    extra_leave_days = models.IntegerField(
        verbose_name=("Jours de congé supplémentaire"),
        help_text=("Veuillez entrer le nombre de jours de congé supplémentaire."),
        default=0
    )

    class Meta:
        verbose_name = "Ancienneté"
        verbose_name_plural = "Anciennetés"

    def __str__(self):
        return self.id
