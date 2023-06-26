from django.urls import path
from . import views

app_name = "linker"
urlpatterns = [
    path('<str:short>/', views.short2original, name='short_link_2_orginal')
]