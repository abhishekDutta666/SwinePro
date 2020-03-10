from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

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


@login_required(login_url='loginuser')
def successupdate(request):
    return render(request,"successupdate.html", context={'tablename':'Update Successful'})
@login_required(login_url='loginuser')
def updateform(request):
    return render(request,"update.html", context={'tablename':'Update Information'})

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
            form.save()
            return redirect('create_nutrition',animal_id=str(form.cleaned_data['animal_id']))
    context={
        'form':form,
        'tablename': 'General Indentification And Parentage'
    }

    return render(request,"create/create_general.html",context)

@login_required(login_url='loginuser')
def create_disposal(request,animal_id):
    form=disposal_form(initial={'gip':animal_id})
    if request.method=='POST':    
        form=disposal_form(request.POST)
        if form.is_valid():
            form.save()
            print("I was here")
            return redirect('dbsuccess')
    context={
        'form':form,
        'tablename':'Disposal And Culling'
    }

    return render(request,"create/create_disposal.html",context)

@login_required(login_url='loginuser')
def create_nutrition(request,animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=nutrition_form(initial={'gip':animal})
    if request.method=='POST':
        print("Pooooosssssttttt")    
        form=nutrition_form(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            print("saved")
            return redirect('create_efficiency',animal_id=animal_id)
    context={
        'form':form,
        'tablename': 'Nutrition And Feeding'
    }

    return render(request,"create/create_nutrition.html",context)

@login_required(login_url='loginuser')
def create_economics(request,animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=economics_form(initial={'gip':animal})
    if request.method=='POST':
        form=economics_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_disposal',animal_id=animal_id)
    context={
        'form':form,
        'tablename':'Economics'
    }

    return render(request,"create/create_economics.html",context)

@login_required(login_url='loginuser')
def create_efficiency(request,animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=efficiency_form(initial={'gip':animal})
    if request.method=='POST':    
        form=efficiency_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_qualification',animal_id=animal_id)
    context={
        'form':form,
        'tablename':'Efficiency Parameter'
    }

    return render(request,"create/create_efficiency.html",context)

@login_required(login_url='loginuser')
def create_qualification(request,animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
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
def create_service(request,animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=service_form(initial={'gip':animal})
    if request.method=='POST':    
        form=service_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_economics',animal_id=animal_id)
    context={
        'form':form,
        'tablename': 'Service Record And Litter Character'
    }

    return render(request,"create/create_service.html",context)


@login_required(login_url='loginuser')
def update_general(request, animal_id):
    animal=general_identification_and_parentage.objects.get(animal_id=animal_id)
    form=general_form(instance=animal)
    if request.method=='POST':
        form=general_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'General Indentification And Parentage'
    }

    return render(request,"formtemplate.html",context)


@login_required(login_url='loginuser')
def update_disposal(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=disposal_culling.objects.get(gip=obj)
    form=disposal_form(instance=animal)
    if request.method=='POST':
        form=disposal_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Disposal/Culling'
    }

    return render(request,"formtemplate.html",context)

@login_required(login_url='loginuser')
def update_nutrition(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=nutrition_and_feeding.objects.get(gip=obj)
    form=nutrition_form(instance=animal)
    if request.method=='POST':
        form=nutrition_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Nutrition And Feeding'
    }

    return render(request,"formtemplate.html",context)

@login_required(login_url='loginuser')
def update_economics(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=economics.objects.get(gip=obj)
    form=economics_form(instance=animal)
    if request.method=='POST':
        form=economics_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Economics'
    }

    return render(request,"formtemplate.html",context)

@login_required(login_url='loginuser')
def update_efficiency(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=efficiency_parameter.objects.get(gip=obj)
    form=efficiency_form(instance=animal)
    if request.method=='POST':
        form=efficiency_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Efficiency Parameter'
    }

    return render(request,"formtemplate.html",context)

@login_required(login_url='loginuser')
def update_qualification(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=qualification_boar.objects.get(gip=obj)
    form=qualification_form(instance=animal)
    if request.method=='POST':
        form=qualification_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Qualification As A Breeding Boar'
    }

    return render(request,"formtemplate.html",context)

@login_required(login_url='loginuser')
def update_service(request, animal_id):
    obj=general_identification_and_parentage.objects.get(animal_id=animal_id)
    animal=service_record.objects.get(gip=obj)
    form=service_form(instance=animal)
    if request.method=='POST':
        form=service_form(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('successupdate')
    context={
        'form':form,
        'tablename': 'Service Record And Litter Character'
    }

    return render(request,"formtemplate.html",context)


    


    