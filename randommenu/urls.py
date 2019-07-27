from django.contrib import admin
from django.urls import path

import roulettehome.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',roulettehome.views.home, name="home"),
    path('bestmenu/',roulettehome.views.bestmenu,name="bestmenu"),
    path('tasteboard/',roulettehome.views.tasteboard,name="tasteboard"),
    path('areaboard/',roulettehome.views.areaboard,name="areaboard"),
    path('bestmenu/koreanFood/<int:koreanFood_id>',roulettehome.views.detail_koreanFood,name="detail_koreanFood"),
    path('bestmenu/new_koreanFood/',roulettehome.views.new_koreanFood,name="new_koreanFood"),
    path('bestmenu/create_koreanFood/',roulettehome.views.create_koreanFood,name="create_koreanFood"),
]
