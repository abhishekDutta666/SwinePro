from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),

    path('dbsuccess/', views.dbsuccess, name='dbsuccess'),
    path('update/success/', views.successupdate, name='successupdate'), 


    path('create/general/', views.create_general, name='create_general'),
    #path('vaccination/',views.create_vaccination, name='vaccination'),
    #path('vetexam/', views.create_vetexam, name='vetexam'),
    path('create/disposal/', views.create_disposal, name='create_disposal'),
    path('create/nutrition/', views.create_nutrition, name='create_nutrition'),
    path('create/economics/', views.create_economics, name='create_economics'),
    path('create/efficiency/', views.create_efficiency, name='create_efficiency'),
    path('create/qualification/', views.create_qualification, name='create_qualification'),
    path('create/service/', views.create_service, name='create_service'),

    path('update/', views.updateform, name='updateform'),
    path('update/general/<str:animal_id>', views.update_general, name='update_general'),
    path('update/disposal/<str:animal_id>', views.update_disposal, name='update_disposal'),
    path('update/nutrition/<str:animal_id>', views.update_nutrition, name='update_nutrition'),
    path('update/economics/<str:animal_id>', views.update_economics, name='update_economics'),
    path('update/efficiency/<str:animal_id>', views.update_efficiency, name='update_efficiency'),
    path('update/qualification/<str:animal_id>', views.update_qualification, name='update_qualification'),
    path('update/service/<str:animal_id>', views.update_service, name='update_service'),
]