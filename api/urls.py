from django.urls import path
from. import views

urlpatterns = [
    path('api/', views.get_data),
    path('add/', views.add_item)
]