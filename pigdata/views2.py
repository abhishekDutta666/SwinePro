from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='loginuser')
def history(request, animal_id):
	animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
	animal_gender=animal.gender
	animal_health_parameter_vaccination=health_parameter_vaccination.objects.values(gip=animal)
	animal_health_parameter_vetexam=health_parameter_vetexam.objects.values(gip=animal)
	animal_disposal_culling=disposal_culling.objects.values(gip=animal)
	animal_nutrition_and_feeding=nutrition_and_feeding.objects.values(gip=animal)
	animal_economics=economics.objects.values(gip=animal)
	if animal_gender=='male':
		animal_efficiency_parameter_male=efficiency_parameter_male.objects.get(gip=animal)
		animal_qualification_boar=qualification_boar.objects.get(gip=animal)
		animal_service_record_male=service_record_male.objects.values(gip=animal)
	elif animal_gender=='female':
		animal_efficiency_parameter_female=efficiency_parameter_female.objects.get(gip=animal)
		animal_service_record_female=service_record_female.objects.values(gip=animal)
		animal_lifetime_litter_character=lifetime_litter_character.objects.

    