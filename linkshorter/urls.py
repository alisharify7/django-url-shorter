from django.urls import path
from . import views

app_name="linkshorter"

urlpatterns = [
    path("", views.index, name='index_view'),
    path("generate_short_url/", views.ConvertUrl2Short, name='generate_short_url_post')
]