from django.urls import path , include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from . import views

#api version
router =  routers.DefaultRouter()
router.register(r'hotelnmp', views.habitacionView, 'hotelnmp')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title='HOTEL NMP API')),
    path('', views.inicio_view, name='inicio'),
    path('reservar/<int:habitacion_id>/', views.reservar_view, name='reservar')
]
