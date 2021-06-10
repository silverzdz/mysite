from django.conf.urls import url, include
import medicine.views as views
from django.urls import path

urlpatterns = [
    path('add_drug',views.add_drug),
    path('show_drugs',views.show_drugs),
    path('buy_drug',views.buy_drug),
    path('delete_drug',views.delete_drug),
]