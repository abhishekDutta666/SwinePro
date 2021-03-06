from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

# for login
#
#
#-----------------------------------------------------------------------------------------------------------------------------------
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    form=loginuserform()
    if request.method=='POST':
        form=loginuserform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, 'username or password is incorrect')

    context={'form': form
    ,'tablename':'Login'}
    return render(request, "login.html", context)

def logoutuser(request):
    logout(request)
    return redirect('loginuser')

def registeruser(request):
    if request.user.is_authenticated:
        return redirect('index')
    form =CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
    context={
    'form':form,
    'tablename':'Register',
    }

    return render(request, "register.html", context)

#--------------------------------------------------------------------------------------------------------------------------------------





















#---------------------------------------------------------------------------------------------------------------------------------------

def dataentry(request):
    return render(request, "dataentry.html", context={'tablename':'What Do You Want To Do ?'})

def report(request):
    return render(request, "report.html", context={'tablename':'Report Generation'})
#-------------------------------------------------------------------------------------------------------------------------------------------






















@login_required(login_url='loginuser')
def delete(request, animal_id):
    animal=get_object_or_404(general_identification_and_parentage, animal_id=animal_id)
    animal.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='loginuser')
def deletepigs(request):
    animals=general_identification_and_parentage.objects.all()
    context={
        'animals':animals,
        'tablename':'Remove Pigs',
    }
    return render(request, "deletepigs.html", context)


@login_required(login_url='loginuser')
def delete_service(request, animal_id, pk):
    if request.method=='POST':
        backbutton=request.POST.get('backbutton')
        animal=get_object_or_404(general_identification_and_parentage, animal_id=animal_id)
        if animal.gender=='Male':
            #service=get_object_or_404(service_record_male, gip=animal, pk=pk)
            service=service_record_male.objects.get(gip=animal, pk=pk) 
            
            service.delete()
            return redirect(backbutton)
        else:
            service=get_object_or_404(service_record_female, gip=animal, pk=pk)
            service.delete()
            return redirect(request.build_absolute_uri())

@login_required(login_url='loginuser')
def delete_vaccination(request, animal_id, pk):
    if request.method=='POST':
        backbutton=request.POST.get('backbutton')
        animal=get_object_or_404(general_identification_and_parentage, animal_id=animal_id)
        vacc=health_parameter_vaccination.objects.get(gip=animal, pk=pk) 
        vacc.delete()
        return redirect(backbutton)

@login_required(login_url='loginuser')
def delete_vetexam(request, animal_id, pk):
    if request.method=='POST':
        backbutton=request.POST.get('backbutton')
        animal=get_object_or_404(general_identification_and_parentage, animal_id=animal_id)
        vet=health_parameter_vetexam.objects.get(gip=animal, pk=pk) 
        vet.delete()
        return redirect(backbutton)

@login_required(login_url='loginuser')
def delete_nutrition(request, animal_id, pk):
    if request.method=='POST':
        backbutton=request.POST.get('backbutton')
        animal=get_object_or_404(general_identification_and_parentage, animal_id=animal_id)
        nutrition=nutrition_and_feeding.objects.get(gip=animal, pk=pk) 
        nutrition.delete()
        return redirect(backbutton)












































#-----------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='loginuser')
def dbsuccess(request):
    return render(request, "dbsuccess.html", context={'tablename':'Success'})

@login_required(login_url='loginuser')
def index(request):
    return render(request, "index.html", context={'tablename':'Welcome'})

@login_required(login_url='loginuser')
def create_general(request):
    form=general_form()
    if request.method=='POST':
        form=general_form(request.POST)
        if form.is_valid():
            animal_id=str(form.cleaned_data['animal_id'])
            if general_identification_and_parentage.objects.filter(animal_id=animal_id).exists()==False:
                form.save()
                return redirect('create_efficiency',animal_id)
            else:
                messages.error(request, 'animal already exists')

    context={
        'form':form,
        'tablename': 'General Identification And Parentage'
    }

    return render(request,"create/create_general.html",context)

@login_required(login_url='loginuser')
def create_efficiency(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    gender=animal.gender
    if gender=='Male':
        form=efficiency_form_male(initial={'gip':animal})
        if request.method=='POST':    
            form=efficiency_form_male(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                agevar=instance.dow-instance.gip.dob
                instance.weaning_age=agevar.days
                form.save()
                return redirect('create_qualification',animal_id=animal_id)
        context={
            'form':form,
            'tablename':'Efficiency Parameter'
        }

        return render(request,"create/create_efficiency_male.html",context)
    elif gender=='Female':
        form=efficiency_form_female(initial={'gip':animal})
        if request.method=='POST':    
            form=efficiency_form_female(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                agevar=instance.dow-instance.gip.dob
                instance.weaning_age=agevar.days
                form.save()
                return redirect('create_qualification',animal_id=animal_id)
        context={
            'form':form,
            'tablename':'Efficiency Parameter'
        }

        return render(request,"create/create_efficiency_female.html",context)

@login_required(login_url='loginuser')
def create_qualification(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    gender=animal.gender
    if gender=='Female':
        return redirect('create_service',animal_id=animal_id)
    
    form=qualification_form(initial={'gip':animal})
    if request.method=='POST':    
        form=qualification_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_service',animal_id=animal_id)
    context={
        'form':form,
        'tablename': 'Qualification As Breeding Boar'
    }

    return render(request,"create/create_qualification.html",context)

@login_required(login_url='loginuser')
def create_service(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    gender=animal.gender
    if gender=='Male':
        services=service_record_male.objects.filter(gip=animal)
        form=service_form_male(initial={'gip':animal})
        if request.method=='POST':    
            form=service_form_male(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                born_total=instance.born_female+instance.born_male
                weaned_total=instance.weaned_female+instance.weaned_male
                instance.total_weaned=weaned_total
                instance.born_total=born_total
                form.save()
                return redirect('create_service',animal_id=animal_id)
        context={
            'form':form,
            'services':services,
            'gip':animal_id,
            'tablename': 'Service Record And Litter Character',
            'backbut':request.build_absolute_uri(),
        }

        return render(request,"service_male.html",context)
    elif gender=='Female':
        services=service_record_female.objects.filter(gip=animal)
        form=service_form_female(initial={'gip':animal})
        if request.method=='POST':    
            form=service_form_female(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                born_total=instance.born_female+instance.born_male
                weaned_total=instance.weaned_female+instance.weaned_male
                instance.total_weaned=weaned_total
                instance.born_total=born_total
                form.save()
                return redirect('create_service',animal_id=animal_id)
        context={
            'form':form,
            'services':services,
            'gip':animal_id,
            'tablename': 'Service Record And Litter Character',
            'backbut':request.build_absolute_uri(),
        }
        return render(request,"service_female.html",context)

@login_required(login_url='loginuser')
def vaccination(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    vaccinations=health_parameter_vaccination.objects.filter(gip=animal)
    form=vaccination_form(initial={'gip':animal})
    if request.method=='POST':    
        form=vaccination_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccination',animal_id=animal_id)
    context={
        'form':form,
        'vaccinations':vaccinations,
        'gip':animal_id,
        'backbut':request.build_absolute_uri(),
        'tablename':'Vaccinations'
    }

    return render(request,"vaccinationtemplate.html",context)

@login_required(login_url='loginuser')
def vetexam(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    vet_exams=health_parameter_vetexam.objects.filter(gip=animal)
    form=vetexam_form(initial={'gip':animal})
    if request.method=='POST':    
        form=vetexam_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vetexam',animal_id=animal_id)
    context={
        'form':form,
        'vet_exams':vet_exams,
        'gip':animal_id,
        'backbut':request.build_absolute_uri(),
        'tablename':'Veterinary Exam'
    }

    return render(request,"vetexamtemplate.html",context)

@login_required(login_url='loginuser')
def deathview(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=death_form(initial={'gip':animal})
    if request.method=='POST':    
        form=death_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_nutrition',animal_id=animal_id)
    context={
        'tablename':'Information About Death Of Pig',
        'form':form,
    }

    return render(request,"create/create_death.html",context)

@login_required(login_url='loginuser')
def create_nutrition(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    nutritions=nutrition_and_feeding.objects.filter(gip=animal)
    form=nutrition_form(initial={'gip':animal})
    if request.method=='POST':
          
        form=nutrition_form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('create_nutrition',animal_id=animal_id)
    context={
        'tablename':'Nutrition',
        'form':form,
        'nutritions': nutritions,
        'backbut':request.build_absolute_uri(),
        'gip':animal_id
    }

    return render(request,"nutrition_template.html",context)


@login_required(login_url='loginuser')
def create_disposal(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=disposal_form(initial={'gip':animal})
    if request.method=='POST':    
        form=disposal_form(request.POST)
        if form.is_valid():
            form.save()
            print("I was here")
            return redirect('create_economics', animal_id=animal_id)
    context={
        'form':form,
        'tablename':'Disposal And Culling'
    }

    return render(request,"create/create_disposal.html",context)





@login_required(login_url='loginuser')
def create_economics(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=economics_form(initial={'gip':animal})
    if request.method=='POST':
        form=economics_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dbsuccess')
    context={
        'form':form,
        'tablename':'Economics'
    }

    return render(request,"create/create_economics.html",context)









#-----------------------------------------------------------------------------------------------------------------------------------












@login_required(login_url='loginuser')
def successupdate(request):
    return render(request,"successupdate.html", context={'tablename':'Update Successful'})
@login_required(login_url='loginuser')
def update(request):
    animal_id=request.POST.get('animal_id')
    if general_identification_and_parentage.objects.filter(animal_id=animal_id).exists():
        animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
        context={'tablename':'Update Records', 'animal_id':animal_id}
        if animal.gender=='Female':
            return render(request,"updatefemale.html",context)
        elif animal.gender=='Male':
            return render(request,"updatemale.html", context)
    else:
        messages.error(request, 'The animal does not exist')
        return redirect(dataentry)


@login_required(login_url='loginuser')
def update_general(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=general_update_form(instance=animal)
    if request.method=='POST':
        form=general_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'General Identification And Parentage'
    }

    return render(request,"create/create_general.html",context)


@login_required(login_url='loginuser')
def update_disposal(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal, create=disposal_culling.objects.get_or_create(gip=obj)
    form=disposal_update_form(instance=animal)
    if request.method=='POST':
        form=disposal_update_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Disposal/Culling'
    }

    return render(request,"create/create_disposal.html",context)


@login_required(login_url='loginuser')
def update_nutrition(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    nutritions=nutrition_and_feeding.objects.filter(gip=animal)
    form=nutrition_form(initial={'gip':animal})
    if request.method=='POST':
          
        form=nutrition_form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('update_nutrition',animal_id=animal_id)
    context={
        'tablename':'Nutrition',
        'form':form,
        'nutritions': nutritions,
        'backbut':request.build_absolute_uri(),
        'gip':animal_id
    }

    return render(request,"nutrition_update_template.html",context)

@login_required(login_url='loginuser')
def update_economics(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal, create=economics.objects.get_or_create(gip=obj)
    form=economics_update_form(instance=animal)
    if request.method=='POST':
        form=economics_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Economics'
    }

    return render(request,"create/create_economics.html",context)

@login_required(login_url='loginuser')
def update_efficiency(request,animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    gender=obj.gender
    if gender=='Male':
        animal, create=efficiency_parameter_male.objects.get_or_create(gip=obj)
        form=efficiency_update_form_male(instance=animal)
        if request.method=='POST':
            form=efficiency_update_form_male(request.POST, instance=animal)
            if form.is_valid():
                instance=form.save(commit=False)
                agevar=instance.dow-instance.gip.dob
                instance.weaning_age=agevar.days
                form.save()
                return redirect('successupdate')
        context={
            'form':form,
            'tablename': 'Efficiency Parameter'
        }

        return render(request,"create/create_efficiency_male.html",context)
    elif gender=='Female':
        animal, create=efficiency_parameter_female.objects.get_or_create(gip=obj)
        form=efficiency_update_form_female(instance=animal)
        if request.method=='POST':
            form=efficiency_update_form_female(request.POST, instance=animal)
            if form.is_valid():
                instance=form.save(commit=False)
                agevar=instance.dow-instance.gip.dob
                instance.weaning_age=agevar.days
                form.save()
                return redirect('successupdate')
        context={
            'form':form,
            'tablename': 'Efficiency Parameter'
        }

        return render(request,"create/create_efficiency_female.html",context)

@login_required(login_url='loginuser')
def update_qualification(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal, create=qualification_boar.objects.get_or_create(gip=obj)
    form=qualification_update_form(instance=animal)
    if request.method=='POST':
        form=qualification_update_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Qualification As A Breeding Boar'
    }

    return render(request,"create/create_qualification.html",context)

@login_required(login_url='loginuser')
def update_death(request, animal_id):
    obj, create=general_identification_and_parentage.objects.get_or_create(animal_id=animal_id)
    animal=death.objects.get(gip=obj)
    form=death_update_form(instance=animal)
    if request.method=='POST':
        form=death_update_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Information about death'
    }

    return render(request,"create/create_death.html",context)

@login_required(login_url='loginuser')
def update_service(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    gender=animal.gender
    if gender=='Male':
        services=service_record_male.objects.filter(gip=animal)
        form=service_form_male(initial={'gip':animal})
        if request.method=='POST':    
            form=service_form_male(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                born_total=instance.born_female+instance.born_male
                weaned_total=instance.weaned_female+instance.weaned_male
                instance.total_weaned=weaned_total
                instance.born_total=born_total
                form.save()
                return redirect('update_service',animal_id=animal_id)
        context={
            'form':form,
            'services':services,
            'gip':animal_id,
            'backbut':request.build_absolute_uri(),
            'tablename': 'Service Record And Litter Character'
        }

        return render(request,"service_update_male.html",context)
    elif gender=='Female':
        services=service_record_female.objects.filter(gip=animal)
        form=service_form_female(initial={'gip':animal})
        if request.method=='POST':    
            form=service_form_female(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                born_total=instance.born_female+instance.born_male
                weaned_total=instance.weaned_female+instance.weaned_male
                instance.total_weaned=weaned_total
                instance.born_total=born_total
                form.save()
                return redirect('update_service',animal_id=animal_id)
        context={
            'form':form,
            'services':services,
            'gip':animal_id,
            'backbut':request.build_absolute_uri(),
            'tablename': 'Service Record And Litter Character'
        }
        return render(request,"service_update_female.html",context)

@login_required(login_url='loginuser')
def update_vaccination(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    vaccinations=health_parameter_vaccination.objects.filter(gip=animal)
    form=vaccination_form(initial={'gip':animal})
    if request.method=='POST':    
        form=vaccination_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_vaccination',animal_id=animal_id)
    context={
        'form':form,
        'vaccinations':vaccinations,
        'gip':animal_id,
        'backbut':request.build_absolute_uri(),
        'tablename':'Vaccinations'
    }

    return render(request,"vaccination_update_template.html",context)

@login_required(login_url='loginuser')
def update_vetexam(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    vet_exams=health_parameter_vetexam.objects.filter(gip=animal)
    form=vetexam_form(initial={'gip':animal})
    if request.method=='POST':    
        form=vetexam_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_vetexam',animal_id=animal_id)
    context={
        'form':form,
        'vet_exams':vet_exams,
        'gip':animal_id,
        'backbut':request.build_absolute_uri(),
        'tablename':'Veterinary Exam'
    }

    return render(request,"vetexam_update_template.html",context)





# @login_required(login_url='loginuser')
# def update_service(request, animal_id):
#     obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
#     gender=obj.gender
#     if gender=='Male':
#         animal=service_record_male.objects.get(gip=obj)
#         form=service_update_form_male(instance=animal)
#         if request.method=='POST':
#             form=service_update_form_male(request.POST, instance=animal)
#             if form.is_valid():
#                 form.save()
#                 return redirect('successupdate')
#         context={
#             'form':form,
#             'tablename': 'Service Record And Litter Character'
#         }

#         return render(request,"formtemplate.html",context)
#     elif gender=='Female':
#         animal=service_record_female.objects.get(gip=obj)
#         form=service_update_form_female(instance=animal)
#         if request.method=='POST':
#             form=service_update_form_female(request.POST, instance=animal)
#             if form.is_valid():
#                 form.save()
#                 return redirect('successupdate')
#         context={
#             'form':form,
#             'tablename': 'Service Record And Litter Character'
#         }

#-----------------------------------------------------------------------------------------------------------------------------






















@login_required(login_url='loginuser')
def history(request, animal_id):
    if general_identification_and_parentage.objects.filter(animal_id=animal_id).exists()==False:
        messages.error(request, 'The animal does not exist')
        return redirect(report)
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal_gender=animal.gender
    animal_health_parameter_vaccination=health_parameter_vaccination.objects.filter(gip=animal)
    animal_health_parameter_vetexam=health_parameter_vetexam.objects.filter(gip=animal)
    if disposal_culling.objects.filter(gip=animal).exists()==True:
        animal_disposal_culling=disposal_culling.objects.get(gip=animal)
    else:
        animal_disposal_culling=None
    animal_nutrition_and_feeding=nutrition_and_feeding.objects.filter(gip=animal)
    if economics.objects.filter(gip=animal)==True:
        animal_economics=economics.objects.get(gip=animal)
    else:
        animal_economics=None
    if death.objects.filter(gip=animal).exists()==True:
        animal_death=death.objects.get(gip=animal)
    else:
        animal_death=None
    if animal_gender=='Male':
        if efficiency_parameter_male.objects.filter(gip=animal)==True:
            animal_efficiency_parameter_male=efficiency_parameter_male.objects.get(gip=animal)
        else:
            animal_efficiency_parameter_male=None
        if qualification_boar.objects.filter(gip=animal)==True:
            animal_qualification_boar=qualification_boar.objects.get(gip=animal)
        else:
            animal_qualification_boar=None
        animal_service_record_male=service_record_male.objects.filter(gip=animal)
        context={
        'tablename':'History Sheet',
        'death':animal_death,
        'gen':animal,
        'vaccinations':animal_health_parameter_vaccination,
        'vetexams':animal_health_parameter_vetexam,
        'disposal':animal_disposal_culling,
        'nutritions':animal_nutrition_and_feeding,
        'economic':animal_economics,
        'efficiency':animal_efficiency_parameter_male,
        'qualification':animal_qualification_boar,
        'services':animal_service_record_male
        }
        return render(request, "historydatamale.html", context)
    
    elif animal_gender=='Female':
        if efficiency_parameter_female.objects.filter(gip=animal)==True:
            animal_efficiency_parameter_female=efficiency_parameter_female.objects.get(gip=animal)
        else:
            animal_efficiency_parameter_female=None
        
        animal_service_record_female=service_record_female.objects.filter(gip=animal)
        for i in animal_service_record_female:
            born_sum+=i.born_total
            weaned_sum+=i.total_weaned
            total_born_weight+=i.litter_weight_birth
            total_weaned_weight+=i.weaning_weight
        preweaning_mortality=(born_sum-weaned_sum)*100.0/born_sum
        #animal_lifetime_litter_character=lifetime_litter_character.objects.get(gip=animal)
        context={
        'tablename':'History Sheet',
        'death':death,
        'gen':animal,
        'vaccinations':animal_health_parameter_vaccination,
        'vetexams':animal_health_parameter_vetexam,
        'disposal':animal_disposal_culling,
        'nutritions':animal_nutrition_and_feeding,
        'economic':animal_economics,
        'services':animal_service_record_female,
        'efficiency':animal_efficiency_parameter_female,
        'born_sum':born_sum,
        'weaned_sum':weaned_sum,
        'total_born_weight':total_born_weight,
        'total_weaned_weight':total_weaned_weight,
        'preweaning_mortality':preweaning_mortality,
        #'litter':animal_lifetime_litter_character
        }
        return render(request, "historydatafemale.html", context)

@login_required(login_url='loginuser')
def allpigs(request):
    animals=general_identification_and_parentage.objects.all()
    context={
        'animals':animals,
        'tablename':'All The Pigs In The Farm',
    }
    return render(request, "allpigs.html", context)



@login_required(login_url='loginuser')
def pigletborn(request):
    if request.method=='POST':
        form=datetodate(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data['from_date']
            todate=form.cleaned_data['to_date']
            allborn=general_identification_and_parentage.objects.filter(dob__range=(fromdate,todate))
            totalcount=0
            femalecount=0
            malecount=0
            for pig in allborn:
                totalcount+=1
                if pig.gender=='Male':
                    malecount+=1
                elif pig.gender=='Female':
                    femalecount+=1
            context={
                'tablename':'Number of piglet Born',
                'malecount':malecount,
                'femalecount':femalecount,
                'totalcount':totalcount,
                'form':form
            }
            return render(request, "pigletborn.html",context)



    form=datetodate()
    context={
                'tablename':'Number of piglet Born',
                'malecount':'no input',
                'femalecount':'no input',
                'totalcount':'no input',
                'form':form
            }
    return render(request, "pigletborn.html", context)


@login_required(login_url='loginuser')
def pigletweaned(request):
    if request.method=='POST':
        form=datetodate(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data['from_date']
            todate=form.cleaned_data['to_date']
            allweanedmale=efficiency_parameter_male.objects.filter(dow__range=(fromdate,todate))
            allweanedfemale=efficiency_parameter_female.objects.filter(dow__range=(fromdate,todate))
            totalcount=0
            femalecount=0
            malecount=0
            maleweight=0
            femaleweight=0
            for pig in allweanedmale:
                totalcount+=1
                malecount+=1
                maleweight+=pig.weaning_weight
            for pig in allweanedfemale:
                femalecount+=1
                femaleweight+=pig.weaning_weight
            context={
                'tablename':'Piglets Weaned',
                'malecount':malecount,
                'femalecount':femalecount,
                'totalcount':totalcount,
                'maleweight':maleweight,
                'femaleweight':femaleweight,
                'form':form
            }
            return render(request, "pigletweaned.html",context)
    form=datetodate()
    context={
                'tablename':'Piglets Weaned',
                'malecount':'no input',
                'femalecount':'no input',
                'totalcount':'no input',
                'maleweight':'no input',
                'femaleweight':'no input',
                'form':form
            }
    return render(request, "pigletweaned.html", context)



@login_required(login_url='loginuser')
def pigmortality(request):
    if request.method=='POST':
        form=datetodate(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data['from_date']
            todate=form.cleaned_data['to_date']
            alldead=death.objects.filter(date_death__range=(fromdate,todate))
            print(alldead)
            preweaning=0
            postweaning=0
            for pig in alldead:
                print(pig.gip.gender)
                if pig.gip.gender=='Male':
                    obj=efficiency_parameter_male.objects.get(gip=pig.gip)
                    if obj.dow==None:
                        preweaning+=1
                    else:
                        postweaning+=1
                if pig.gip.gender=='Female':
                    obj=efficiency_parameter_female.objects.get(gip=pig.gip)
                    if obj.dow==None:
                        preweaning+=1
                    else:
                        postweaning+=1
            context={
                'tablename':'Pig Mortality',
                'form':form,
                'postweaning':postweaning,
                'preweaning':preweaning,
            }
            return render(request, "pigmortality.html",context)
    form=datetodate()
    context={
                'tablename':'Pig Mortality',
                'form':form,
                'postweaning':None,
                'preweaning':None,
            }
    return render(request, "pigmortality.html", context)


@login_required(login_url='loginuser')
def revenue_received(request):
    if request.method=='POST':
        form=datetodate(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data['from_date']
            todate=form.cleaned_data['to_date']
            revenues=disposal_culling.objects.filter(sale_date__range=(fromdate,todate))
            total=0
            for r in revenues:
                total+=r.revenue
            context={
                'tablename':'Revenue Received',
                'form':form,
                'total':total
            }
            return render(request, "revenuereceived.html",context)
    form=datetodate()
    context={
                'tablename':'Revenue Received',
                'form':form,
                'total':None
            }
    return render(request, "revenuereceived.html", context)

@login_required(login_url='loginuser')
def selectpigs(request):
    if request.method=='POST':
        form=selectpigsform(request.POST)
        if form.is_valid():
            n=form.cleaned_data['task']
            num=form.cleaned_data['amount']
            male=[]
            female=[]
            if n=='1':
                animals=general_identification_and_parentage.objects.filter(colitter_size_of_birth__lt=num)
                len_maleanimals=0
                len_femaleanimals=0
                for i in animals:
                    if i.gender=='Male':
                        male.append(i.animal_id)
                        len_maleanimals+=1
                    else:
                        female.append(i.animal_id)
                        len_femaleanimals+=1
                
            elif n=='2':
                animals=general_identification_and_parentage.objects.filter(colitter_size_of_birth__gt=num)
                len_maleanimals=0
                len_femaleanimals=0
                for i in animals:
                    if i.gender=='Male':
                        male.append(i.animal_id)
                        len_maleanimals+=1
                    else:
                        female.append(i.animal_id)
                        len_femaleanimals+=1
                
            elif n=='3':
                maleanimals=efficiency_parameter_male.objects.filter(litter_size_weaning__gte=num)
                for i in maleanimals:
                    male.append(i.gip)
                femaleanimals=efficiency_parameter_female.objects.filter(litter_size_weaning__gte=num)
                for i in femaleanimals:
                    female.append(i.gip)
                len_maleanimals=len(maleanimals)
                len_femaleanimals=len(femaleanimals)
                
            elif n=='4':
                maleanimals=efficiency_parameter_male.objects.filter(litter_size_weaning__exact=num)
                for i in maleanimals:
                    male.append(i.gip)
                len_maleanimals=len(maleanimals)
                femaleanimals=efficiency_parameter_female.objects.filter(litter_size_weaning__exact=num)
                for i in femaleanimals:
                    female.append(i.gip)
                len_femaleanimals=len(femaleanimals)
            
            context={
                'form':form,
                'male': male,
                'female': female,
                'malelen': len_maleanimals,
                'femalelen': len_femaleanimals,
                'tablename':'Select Pigs'
            }
            
            return render(request, "selectpigs.html",context)
    form=selectpigsform()
    return render(request, "selectpigs.html", {'form':form, 'tablename':'Select Pigs'})




@login_required(login_url='loginuser')
def disease(request):
    alldeath=death.objects.all()
    diseaseDict={}
    for i in alldeath:
        cause=i.cause_death
        if cause in diseaseDict:
            diseaseDict[cause]+=1
        else:
            diseaseDict[cause]=1
    context={
        'tablename':'Disease List',
        'diseases':diseaseDict
    }
    return render(request, "disease.html", context)