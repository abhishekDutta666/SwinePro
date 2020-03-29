from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput

class datetodate(forms.Form):
    from_date=forms.DateField(label='From')
    to_date=forms.DateField(label='To')

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2']
        labels={'username': 'Username'}
        

class loginuserform(forms.Form):
    username=forms.CharField(label='Username', max_length=150)
    password=forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput)

class general_form(forms.ModelForm):
    class Meta:
        model=general_identification_and_parentage
        fields='__all__'
        labels = {
            'animal_id':'Identification Number',
            'dob':'Date Of Birth',
            'gender':'gender',
            'breed':'Breed',
            'dam_no': 'DAM Number',
            'sire_no': 'SIRE Number',
            'grand_dam': 'Great DAM',
            'grand_sire': 'Grand SIRE',
            'colitter_size_of_birth': 'Colitter Size Of Birth',
            'color_and_marking':'Colors And Markings',
            'abnormalities': 'Genetic Abnormalities/Disorder',
        }
        widgets = {
            'dob': DatePickerInput(format='%Y-%m-%d'),
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
            'revenue':'Revenue Generated'
            
        }
        widgets = {
            'sale_date': DatePickerInput(format='%Y-%m-%d'),
        }

class death_form(forms.ModelForm):
    class Meta:
        model=death
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'cause_death': 'Cause Of Death',
            'date_death': 'Date Of Death',
            'postmortem_findings':'Post Mortem Findings'
        }
        widgets = {
            'date_death': DatePickerInput(format='%Y-%m-%d'),
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
        widgets = {
            'start_date': DatePickerInput(format='%Y-%m-%d'),
            'end_date': DatePickerInput(format='%Y-%m-%d'),
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

class vaccination_form(forms.ModelForm):
    class Meta:
        model=health_parameter_vaccination
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'disease': 'Against Disease',
            'make': 'Make',
            'first_dose': 'First Dose',
            'booster': 'Booster Dose',
        }
        widgets = {
            'first_dose': DatePickerInput(format='%Y-%m-%d'),
            'booster': DatePickerInput(format='%Y-%m-%d'),
            'repeat': DatePickerInput(format='%Y-%m-%d'),
        }

class vetexam_form(forms.ModelForm):
    class Meta:
        model=health_parameter_vetexam
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'reason': 'Reason/Symptoms',
            'date_of_treatment': 'Date of Treatment',
            'medication': 'Medication',
            'remarks': 'Remarks',
        }
        widgets = {
            'date_of_treatment': DatePickerInput(format='%Y-%m-%d'),
        }

class efficiency_form_female(forms.ModelForm):
    class Meta:
        model=efficiency_parameter_female
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'litter_size_weaning':'Litter Size At Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Male Animal',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weight_eight':'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }
        widgets = {
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dosm': DatePickerInput(format='%Y-%m-%d'),
        }


class efficiency_form_male(forms.ModelForm):
    class Meta:
        model=efficiency_parameter_male
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'litter_size_weaning':'Litter Size At Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Female Animal',
            'doc': 'Date of Castration',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weight_eight': 'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }
        widgets = {
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'doc': DatePickerInput(format='%Y-%m-%d'),
            'dosm': DatePickerInput(format='%Y-%m-%d'),
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
        widgets = {
            'date_of_training': DatePickerInput(format='%Y-%m-%d'),
            
        }

class service_form_male(forms.ModelForm):
    class Meta:
        model=service_record_male
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
        widgets = {
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dof': DatePickerInput(format='%Y-%m-%d'),
        }

class service_form_female(forms.ModelForm):
    class Meta:
        model=service_record_female
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'boar_no':'Boar Number',
            'dos': 'Date of Service',
            'nos': 'Nature Of Service',
            'dof': 'Date Of Farrowing',
            'dow': 'Date of Weaning',
            'interfarrowing_interval':'Interfarrowing Interval',
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
            'date_of_abortion':'Date Of Abortion',
        }
        widgets = {
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dof': DatePickerInput(format='%Y-%m-%d'),
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'date_of_abortion': DatePickerInput(format='%Y-%m-%d'),
        }
















class general_update_form(forms.ModelForm):
    class Meta:
        model=general_identification_and_parentage
        fields='__all__'
        labels = {
            'animal_id':'Identification Number',
            'dob':'Date Of Birth',
            'gender':'gender',
            'breed':'Breed',
            'dam_no': 'DAM Number',
            'sire_no': 'SIRE Number',
            'grand_dam': 'Great DAM',
            'grand_sire': 'Grand SIRE',
            'colitter_size_of_birth': 'Colitter Size Of Birth',
            'color_and_marking':'Colors And Markings',
            'abnormalities': 'Genetic Abnormalities/Disorder',
        }
        widgets = {
            'dob': DatePickerInput(format='%Y-%m-%d'),
        }
        
class disposal_update_form(forms.ModelForm):
    class Meta:
        model=disposal_culling
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'reason': 'Reason For Sale/Transfer',
            'sale_date': 'Date Of Sale/Transfer',
            'weight_sale': 'Weight At Sale/Transfer',
            'revenue':'Revenue Generated'
        }
        widgets = {
            'sale_date': DatePickerInput(format='%Y-%m-%d'),
        }

class death_update_form(forms.ModelForm):
    class Meta:
        model=death
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'cause_death': 'Cause Of Death',
            'date_death': 'Date Of Death',
            'postmortem_findings':'Post Mortem Findings'
        }
        widgets = {
            'date_death': DatePickerInput(format='%Y-%m-%d'),
        }



class nutrition_update_form(forms.ModelForm):
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
        widgets = {
            'start_date': DatePickerInput(format='%Y-%m-%d'),
            'end_date': DatePickerInput(format='%Y-%m-%d'),
        }

class economics_update_form(forms.ModelForm):
    class Meta:
        model=economics
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'book_value': 'Book Value',
            'amount_realized': 'Amount Realized',
        }

class vaccination_update_form(forms.ModelForm):
    class Meta:
        model=health_parameter_vaccination
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'disease': 'Against Disease',
            'make': 'Make',
            'first_dose': 'First Dose',
            'booster': 'Booster Dose',
        }
        widgets = {
            'first_dose': DatePickerInput(format='%Y-%m-%d'),
            'booster': DatePickerInput(format='%Y-%m-%d'),
            'repeat': DatePickerInput(format='%Y-%m-%d'),
        }

class vetexam_update_form(forms.ModelForm):
    class Meta:
        model=health_parameter_vetexam
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'reason': 'Reason/Symptoms',
            'date_of_treatment': 'Date of Treatment',
            'medication': 'Medication',
            'remarks': 'Remarks',
        }
        widgets = {
            'date_of_treatment': DatePickerInput(format='%Y-%m-%d'),
        }

class efficiency_update_form_female(forms.ModelForm):
    class Meta:
        model=efficiency_parameter_female
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'litter_size_weaning':'Litter Size At Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Male Animal',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weight_eight': 'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }
        widgets = {
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dosm': DatePickerInput(format='%Y-%m-%d'),
        }


class efficiency_update_form_male(forms.ModelForm):
    class Meta:
        model=efficiency_parameter_male
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'dow': 'Date Of Weaning',
            'litter_size_weaning':'Litter Size At Weaning',
            'weaning_age': 'Age At Weaning',
            'weaning_weight': 'Weaning Weight',
            'dos': 'Date of Separation From Female Animal',
            'doc': 'Date of Castration',
            'dosm': 'Date of Sexual Maturity',
            'sexual_maturity_weight': 'Weight At Sexual Maturity',
            'weight_six': 'Weight At Six Months',
            'weight_eight': 'Weight At Eight Months',
            'conform_at_eight': 'Conformation At Eight Months',
        }
        widgets = {
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'doc': DatePickerInput(format='%Y-%m-%d'),
            'dosm': DatePickerInput(format='%Y-%m-%d'),
        }

class qualification_update_form(forms.ModelForm):
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
        widgets = {
            'date_of_training': DatePickerInput(format='%Y-%m-%d'),
            
        }

class service_update_form_male(forms.ModelForm):
    class Meta:
        model=service_record_male
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
        widgets = {
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dof': DatePickerInput(format='%Y-%m-%d'),
        }

class service_update_form_female(forms.ModelForm):
    class Meta:
        model=service_record_female
        fields='__all__'
        labels={
            'gip': 'Identification Number',
            'boar_no':'Boar Number',
            'dos': 'Date of Service',
            'nos': 'Nature Of Service',
            'dof': 'Date Of Farrowing',
            'dow': 'Date of Weaning',
            'interfarrowing_interval':'Interfarrowing Interval',
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
            'date_of_abortion':'Date Of Abortion',
        }
        widgets = {
            'dos': DatePickerInput(format='%Y-%m-%d'),
            'dof': DatePickerInput(format='%Y-%m-%d'),
            'dow': DatePickerInput(format='%Y-%m-%d'),
            'date_of_abortion': DatePickerInput(format='%Y-%m-%d'),
        }
