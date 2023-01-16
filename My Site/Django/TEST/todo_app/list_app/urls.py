from django.urls import path
# import list_app.views as views
from list_app.views import home


urlpatterns = [
    # path('', views.home, name='home')
    path('', home, name='home')
]
