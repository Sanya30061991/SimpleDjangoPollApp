from django.urls import path
from . import views
urlpatterns = [
    path('show', views.show, name = 'polls'),
    path('logout', views.loggggg, name = 'logoff'),
    path('vote', views.vote, name = 'vote'),
    path('results', views.res, name = 'results')
]