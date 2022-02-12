
from django.contrib import admin
from django.urls import path

from app import views
from app.views import home , login , signup , add_todo , signout , delete_todo, change_todo, second, youtube


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ),
   path('second/',views.second),
   path('youtube/',views.youtube),
   path('contact/',views.contact)

]
