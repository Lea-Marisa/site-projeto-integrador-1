from django.urls import path
from . import views


app_name="principal"
urlpatterns = [
    path('', views.index, name='index'),
    path('calculadora/',views.calculadora, name="calculadora")

]