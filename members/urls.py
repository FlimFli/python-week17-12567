from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', view.member_data, name='member_data'),
]