from django.urls import path
from . import views
urlpatterns = [
    path('show', views.show, name = 'polls'),
    path('logout', views.loggggg, name = 'logoff')
]