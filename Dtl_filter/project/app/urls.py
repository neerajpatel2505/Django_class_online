from django.urls import path
from .views import landing,pqr

urlpatterns = [
    path('',landing, name='landing'),
    path('abc/',pqr,name='xyz')
    
]
