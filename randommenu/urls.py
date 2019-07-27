from django.contrib import admin
from django.urls import path

import roulettehome.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',roulettehome.views.home, name="home"),
]
