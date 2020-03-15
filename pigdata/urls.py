from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.loginuser, name='loginuser'),
    path('register/', views.registeruser, name='registeruser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dataentry/', views.dataentry, name='logoutuser'),
    path('report/', views.report, name='logoutuser'),
    path('dbsuccess/', views.dbsuccess, name='dbsuccess'),
    path('update/', views.update, name='update'),
    path('update/success/', views.successupdate, name='successupdate'), 
    path('create/death/<str:animal_id>', views.deathview, name='deathview'),
    path('create/general/', views.create_general, name='create_general'),
    path('vaccination/<str:animal_id>',views.vaccination, name='vaccination'),
    path('vetexam/<str:animal_id>', views.vetexam, name='vetexam'),
    path('create/disposal/<str:animal_id>', views.create_disposal, name='create_disposal'),
    path('nutrition/<str:animal_id>', views.create_nutrition, name='create_nutrition'),
    path('create/economics/<str:animal_id>', views.create_economics, name='create_economics'),
    path('create/efficiency/<str:animal_id>', views.create_efficiency, name='create_efficiency'),
    path('create/qualification/<str:animal_id>', views.create_qualification, name='create_qualification'),
    path('service/<str:animal_id>', views.create_service, name='create_service'),

    path('update/general/<str:animal_id>', views.update_general, name='update_general'),
    path('update/disposal/<str:animal_id>', views.update_disposal, name='update_disposal'),
    path('update/economics/<str:animal_id>', views.update_economics, name='update_economics'),
    path('update/efficiency/<str:animal_id>', views.update_efficiency, name='update_efficiency'),
    path('update/qualification/<str:animal_id>', views.update_qualification, name='update_qualification'),


    path('history/<str:animal_id>', views.history, name='history'),
    path('pigletborn', views.pigletborn, name='pigletborn'),
    path('pigletweaned', views.pigletweaned, name='pigletweaned'),
    path('pigmortality', views.pigmortality, name='pigmortality'),
    path('revenue', views.revenue_received, name='revenue_received'),
    path('selectpigs', views.selectpigs, name='selectpigs'),
    path('disease', views.disease, name='disease'),
]