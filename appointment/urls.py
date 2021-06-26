import appointment.views as views
from django.urls import path

urlpatterns = [
    path('add_register',views.add_register),
    path('add_covid',views.add_covid),
    path('check_register',views.check_register),
    path('check_covid',views.check_covid),
    path('get_r_id',views.get_r_id),
    path('get_c_id',views.get_c_id),
]