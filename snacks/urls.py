from django.urls import path,include
from .views import Snacks,SnackList
urlpatterns = [
    path('',SnackList.as_view(),name='snack')
]