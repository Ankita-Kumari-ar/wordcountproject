from django.urls import path
from . import views
app_name="wordcount"
urlpatterns=[
    path("",views.countword,name="countword"),
]