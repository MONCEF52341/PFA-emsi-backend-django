from django import forms
from .models import *

class CollaborateurForm(forms.ModelForm):
    class Meta:
        model = Collaborateur
        fields = '__all__'

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