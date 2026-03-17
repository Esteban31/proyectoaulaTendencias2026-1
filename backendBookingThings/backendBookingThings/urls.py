from django.contrib import admin
from django.urls import path, include
from django.db import router


from backendBookingThings.router.router import router


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
  
  