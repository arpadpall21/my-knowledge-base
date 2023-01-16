from django.contrib import admin
from django.urls import path, include

# import list_app.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list_app.urls')),
    
    # path('', views.home),
]
