from django.urls import path
import newApp.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('demo/demo', views.demo, name='demo'),
]