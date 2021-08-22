from django.urls import path
from . import views

app_name = 'pythagoras'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('report/', views.report, name='report'),
]
