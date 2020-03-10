from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2']
        labels={'username': 'Identification'}

class loginuserform(forms.Form):
    username=forms.CharField(label='Identification', max_length=150)
    password=forms.CharField(label='Password', max_length=150)

class general_form(forms.ModelForm):
    class Meta:
        model=general_identification_and_parentage
        fields='__all__'
        labels = {
            'animal_id':'Identification Number',
            'breed':'Breed',
            'dam_no': 'DAM Number',
            'sire_no': 'SIRE Number',
            'grand_dam': 'Great DAM',
            'grand_sire': 'Grand SIRE',
            'colitter_size_of_birth': 'Colitter Size Of Birth',
            'color_and_marking':'Colors And Markings',
            'abnormalities': 'Genetic Abnormalities/Disorder',
        }

class disposal_form(forms.ModelForm):
    class Meta:
        model=disposal_culling
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'reason': 'Reason For Sale/Transfer',
            'sale_date': 'Date Of Sale/Transfer',
            'weight_sale': 'Weight At Sale/Transfer',
            'cause_death': 'Cause Of Death',
            'date_death': 'Date Of Death',
        }

class nutrition_form(forms.ModelForm):
    class Meta:
        model=nutrition_and_feeding
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'treatment': 'Treatment',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'remarks': 'Remarks',
        }

class economics_form(forms.ModelForm):
    class Meta:
        model=economics
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'book_value': 'Book Value',
            'amount_realized': 'Amount Realized',
        }

class efficiency_form_male(forms.ModelForm):
    class Meta:
        model=efficiency_parameter
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Female Animal',
            'doc': 'Date of Castration',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weaning_eight': 'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }

class efficiency_form_female(forms.ModelForm):
    class Meta:
        model=efficiency_parameter
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Female Animal',
            'doc': 'Date of Castration',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weaning_eight': 'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }

class qualification_form(forms.ModelForm):
    class Meta:
        model=qualification_boar
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'physical_fitness': 'Physical Fitness',
            'date_of_training': 'Date Of Onset Of Training',
            'period_of_training': 'Period Of Training',
            'training_score': 'Training Score',
            'seminal_characteristics': 'Evaluation Based On Seminal Characteristics',
            'suitability': 'Suitability For Insemination',
        }

class service_form_male(forms.ModelForm):
    class Meta:
        model=service_record
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'sow_no': 'SOW Number',
            'dos': 'Date of Service',
            'dof': 'Date Of Farrowing',
            'parity': 'Parity',
            'born_male': 'Number of male born',
            'born_female': 'Number of male born',
            'born_total': 'Total Number',
            'litter_weight_birth': 'Litter Weight At Birth',
            'weaned_male': 'Number Of Weaned Male',
            'weaned_female': 'Number Of Weaned Female',
            'total_weaned': 'Number Of Total Weaned',
            'weaning_weight': 'Weaning Weight',
            'still_birth_abnormality': 'Still Birth Or Abnormality',
        }

class service_form_female(forms.ModelForm):
    class Meta:
        model=service_record
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'sow_no': 'SOW Number',
            'dos': 'Date of Service',
            'dof': 'Date Of Farrowing',
            'parity': 'Parity',
            'born_male': 'Number of male born',
            'born_female': 'Number of male born',
            'born_total': 'Total Number',
            'litter_weight_birth': 'Litter Weight At Birth',
            'weaned_male': 'Number Of Weaned Male',
            'weaned_female': 'Number Of Weaned Female',
            'total_weaned': 'Number Of Total Weaned',
            'weaning_weight': 'Weaning Weight',
            'still_birth_abnormality': 'Still Birth Or Abnormality',
        }
