import appointment.views as views
from django.urls import path

urlpatterns = [
    path('add_register',views.add_register),
    path('add_covid',views.add_covid),
]