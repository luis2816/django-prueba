from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view(),  name='prueba'),
    path('crear/', views.PruebaCreateView.as_view(),  name='crear'),
    path('lista/', views.PruebaListView.as_view(),  name='lista'),
    path('prueba/<int:pk>/editar/', views.PruebaUpdateView.as_view(), name='actualizar'),
    path('prueba/<int:pk>/eliminar/', views.PruebaDeleteView.as_view(), name='eliminar'),

]

