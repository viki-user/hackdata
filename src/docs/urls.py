from django.urls import path
from .views import home,report

urlpatterns = [
    path('',home,name='home'  ),
    path('report/', report, name='report' ),

]

 