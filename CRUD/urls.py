from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('events/add/', views.addEvent, name='addEvent'),
    path('events/edit/<int:id>', views.editEvent, name='editEvent'),
    path('events/delete/<int:id>', views.deleteEvent, name='deleteEvent'),

    #Aqui se agregan las rutas para el CRUD de usuarios
    path('users/', views.users, name='users'),
    path('users/add/', views.addUser, name='addUser'),

    #Aqui se agregan las rutas para el registro de eventos
    path('events/records/', views.listRecords, name='records'),
    path('statistics/', views.statistics_view, name='statistics'),

]