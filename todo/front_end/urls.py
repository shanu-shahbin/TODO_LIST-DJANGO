from django.urls import path

from front_end import views

urlpatterns = [

    path('', views.home, name="home"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update")

]
