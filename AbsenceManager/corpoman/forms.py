from django import forms
from .models import *

class CollaborateurForm(forms.ModelForm):
    class Meta:
        model = Collaborateur
        fields = '__all__'
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'})
        }
class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'

class EntiteJuridiqueForm(forms.ModelForm):
    class Meta:
        model = EntiteJuridique
        fields = '__all__'

class LieuTravailForm(forms.ModelForm):
    class Meta:
        model = LieuTravail
        fields = '__all__'

class EmploiForm(forms.ModelForm):
    class Meta:
        model = Emploi
        fields = '__all__'

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'

class HeuresContractuellesForm(forms.ModelForm):
    class Meta:
        model = HeuresContractuelles
        fields = '__all__'

class PolitiqueAbsencesForm(forms.ModelForm):
    class Meta:
        model = PolitiqueAbsences
        fields = '__all__'

class CompteurAbsencesForm(forms.ModelForm):
    class Meta:
        model = CompteurAbsences
        fields = '__all__'

class TypeAbsenceForm(forms.ModelForm):
    class Meta:
        model = TypeAbsence
        fields = '__all__'

class CycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = '__all__'

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = '__all__'

class SeniorityForm(forms.ModelForm):
    class Meta:
        model = Seniority
        fields = '__all__'

class MyprofileForm(forms.ModelForm):
    class Meta:
        model = Collaborateur
        fields = ['prenom', 'nom', 'date_naissance', 'adresse', 'ville', 'code_postal', 'pays', 'numero_telephone','contact_urgence_nom','contact_urgence_telephone']

        labels = {
            'prenom': 'Prénom',
            'nom': 'Nom',
            'date_naissance': 'Date de naissance',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'code_postal': 'Code postal',
            'pays': 'Pays',
            'numero_telephone': 'Téléphone',
            'contact_urgence_nom': 'Nom de contact en cas d\'urgence',
            'contact_urgence_telephone': 'Téléphone de contact en cas d\'urgence',
        }

class PopulateDatabaseForm(forms.Form):
    number_of_entries = forms.IntegerField(label='Nombre d\'entrées à générer', min_value=1)

class DemandeAbsenceForm(forms.ModelForm):
    class Meta:
        model = DemandeAbsence
        fields = '__all__'
        exclude = ['approbateur','employe']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }