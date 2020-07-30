from django.urls import path, include
from . import views
urlpatterns = [
    path('log', views.logg, name='logg'),
    path('reg', views.regg)
]