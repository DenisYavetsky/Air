from flight_app import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('upload/', views.upload_file),
    path('airports/', views.airports_list, name='AirportsList'),
    path('airport/<str:icao_code>/', views.airport_info, name='AirportInfo'),
]
