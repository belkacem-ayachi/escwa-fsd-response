from django.urls import path
from . import views

app_name = 'UNExamApp'

urlpatterns = [
    path('aggregate', views.aggregate, name='aggregate')
]