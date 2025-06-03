from django.urls import path
from . import views #newly added

urlpatterns = [
    path("", views.index), #the path for our index view
]