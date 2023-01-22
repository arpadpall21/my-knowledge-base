from django.urls import path
import login.views as views


urlpatterns = [
    path('', views.login, name='login')
]