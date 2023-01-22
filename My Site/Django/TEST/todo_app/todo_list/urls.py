from django.urls import path
import todo_list.views as views


urlpatterns = [
    path('', views.list, name='home')
]
