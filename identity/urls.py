import identity.views as views
from django.urls import path

urlpatterns = [
    path('add_patient',views.add_patient),
    path('login_patient',views.login_patient),
    path('add_doctor',views.add_doctor),
    path('login_doctor',views.login_doctor),
    path('add_merchant',views.add_merchant),
    path('login_merchant',views.login_merchant),
    path('add_admin',views.add_admin),
    path('login_admin',views.login_admin),
    path('show_docs',views.show_docs),
    path('show_mers',views.show_mers),
]