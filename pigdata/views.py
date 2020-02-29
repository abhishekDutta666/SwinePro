from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def successupdate(request):
    return render(request,"successupdate.html", context={'tablename':'Update Successful'})

def updateform(request):
    return render(request,"update.html", context={'tablename':'Update Information'})


def dbsuccess(request):
    return render(request, "dbsuccess.html", context={'tablename':'Success'})

def index(request):
    return render(request, "index.html", context={'tablename':'Welcome'})

def create_general(request):
    form=general_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_nutrition')
    context={
        'form':form,
        'tablename': 'General Indentification And Parentage'
    }

    return render(request,"formtemplate.html",context)

def create_disposal(request):
    form=disposal_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dbsuccess')
    context={
        'form':form,
        'tablename':'Disposal And Culling'
    }

    return render(request,"formtemplate.html",context)

def create_nutrition(request):
    form=nutrition_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_efficiency')
    context={
        'form':form,
        'tablename': 'Nutrition And Feeding'
    }

    return render(request,"formtemplate.html",context)

def create_economics(request):
    form=economics_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_disposal')
    context={
        'form':form,
        'tablename':'Economics'
    }

    return render(request,"formtemplate.html",context)

def create_efficiency(request):
    form=efficiency_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_qualification')
    context={
        'form':form,
        'tablename':'Efficiency Parameter'
    }

    return render(request,"formtemplate.html",context)

def create_qualification(request):
    form=qualification_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_service')
    context={
        'form':form,
        'tablename': 'Qualification As Breeding Boar'
    }

    return render(request,"formtemplate.html",context)

def create_service(request):
    form=service_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create_economics')
    context={
        'form':form,
        'tablename': 'Service Record And Litter Character'
    }

    return render(request,"formtemplate.html",context)



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