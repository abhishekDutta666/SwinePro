from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.loginuser, name='loginuser'),
    path('register/', views.registeruser, name='registeruser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dbsuccess/', views.dbsuccess, name='dbsuccess'),
    path('update/success/', views.successupdate, name='successupdate'), 
    path('update/morfupdate/', views.maleorfemaleupdate, name='maleorfemaleupdate'),
    path('update/morfcreate/', views.maleorfemalecreate, name='maleorfemalecreate'),

    path('create/general/<str:gender>/', views.create_general, name='create_general'),
    #path('vaccination/',views.create_vaccination, name='vaccination'),
    #path('vetexam/', views.create_vetexam, name='vetexam'),
    path('create/disposal/<str:gender>/<str:animal_id>', views.create_disposal, name='create_disposal'),
    path('create/nutrition/<str:gender>/<str:animal_id>', views.create_nutrition, name='create_nutrition'),
    path('create/economics/<str:gender>/<str:animal_id>', views.create_economics, name='create_economics'),
    path('create/efficiency/<str:gender>/<str:animal_id>', views.create_efficiency, name='create_efficiency'),
    path('create/qualification/<str:gender>/<str:animal_id>', views.create_qualification, name='create_qualification'),
    path('create/service/<str:gender>/<str:animal_id>', views.create_service, name='create_service'),

    path('update/male', views.updateform, name='updateform'),
    path('update/female', views.updateform, name='updateform'),
    path('update/general/<str:gender>/<str:animal_id>', views.update_general, name='update_general'),
    path('update/disposal/<str:gender>/<str:animal_id>', views.update_disposal, name='update_disposal'),
    path('update/nutrition/<str:gender>/<str:animal_id>', views.update_nutrition, name='update_nutrition'),
    path('update/economics/<str:gender>/<str:animal_id>', views.update_economics, name='update_economics'),
    path('update/male/efficiency/<str:gender>/<str:animal_id>', views.update_efficiency, name='update_efficiency'),
    path('update/female/efficiency/<str:gender>/<str:animal_id>', views.update_efficiency, name='update_efficiency'),
    path('update/qualification/<str:gender>/<str:animal_id>', views.update_qualification, name='update_qualification'),
    path('update/male/service/<str:gender>/<str:animal_id>', views.update_service, name='update_service'),
    path('update/female/service/<str:gender>/<str:animal_id>', views.update_service, name='update_service'),
]