from django.urls import path,include
from .views import Snacks,SnackList
urlpatterns = [
    path('',Snacks.as_view(),name='snack'),
    path('snack_detail/<pk>',SnackList.as_view(),name='SnackList')
]