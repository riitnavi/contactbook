from django.urls import path
from . import views
urlpatterns=[
    path('welcome',views.welcome),
    path('addcontact',views.addcontact),
    path('viewcontact',views.viewcontact),
    path('add_contact_post',views.add_contact_post),
    path('edit_contact_post',views.edit_contact_post),
    

    
    
]