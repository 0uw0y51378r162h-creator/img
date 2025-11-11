from unicodedata import name
from django.urls import path
from .views import SearchList, CreateList, DeleteList

urlpatterns = [
    path('list/', SearchList.as_view(), name='list'),
    path('create/', CreateList.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteList.as_view(), name='delete'),
]