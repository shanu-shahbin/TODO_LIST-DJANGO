from django.urls import path

from front_end import views

urlpatterns = [
    path('', views.index, name="index")

]