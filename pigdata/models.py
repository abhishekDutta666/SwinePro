from django.db import models

class general_identification_and_parentage(models.Model):
    animal_id=models.CharField(max_length=20)
    breed=models.CharField(max_length=20)
    dam_no=models.CharField(max_length=20)

class health_parameter_vaccination(models.Model):
    disease=models.CharField(max_length=50)
    first_dose=models.DateField()


class health_parameter_vetexam(models.Model):
    reason=models.TextField()
    date_of_treatment=models.DateField()

class disposal_culling(models.Model):
    reason=models.TextField()
    sale_date=models.DateField()
    gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)

class nutrition_and_feeding(models.Model):
    treatment=models.TextField()
    start_date=models.DateField()
    #gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)

class economics(models.Model):
    book_value=models.IntegerField()
    amount_realized =models.IntegerField()
    #gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)

class efficiency_parameter(models.Model):
    dow=models.DateField()
    weaning_age=models.IntegerField()
    #gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)

class qualification_boar(models.Model):
    physical_fitness=models.TextField()
    date_of_training=models.DateField()
    #gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)

class service_record(models.Model):
    sow_no=models.CharField(max_length=20)
    dof=models.DateField()
    #gip = models.OneToOneField(general_identification_and_parentage, on_delete=models.CASCADE)