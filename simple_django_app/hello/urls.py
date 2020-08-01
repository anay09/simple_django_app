from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anay', views.anay, name='anay'),
    path('<str:name>', views.greet, name='greet')
]