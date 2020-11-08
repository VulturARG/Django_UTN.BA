from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vistaprevia/', include('vistaprevia.urls')),
    path('admin/', admin.site.urls), 
]
