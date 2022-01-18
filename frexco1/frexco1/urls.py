"""frexco1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frexcoapi import views

urlpatterns = [
    path('', views.index),
    path('regioes/', views.get_region),
    path('frutas/', views.get_fruit),
    path('frutas_por_regiao/', views.get_fruit_region),
    path('regioes_por_id/', views.get_region_id),
    path('frutas_por_id/', views.get_fruit_id),
    path('cadastra_fruta', views.post_fruit),
    path('atualiza_fruta', views.put_fruit),
    path('excluir_fruta', views.delete_fruit),
    path('admin/', admin.site.urls),
]
