from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

import todo_app.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('login/', include('login.urls')),
    path('list/', include('todo_list.urls')),
    path('', RedirectView.as_view(url='login/')),
    
    path('users/', views.users, name='users')
]
