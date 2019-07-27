from django.contrib import admin

from .models import KoreanFood, ChineseFood, JapaneseFood, WesternFood, FastFood, Dessert, Drink

admin.site.register(KoreanFood)
admin.site.register(ChineseFood)
admin.site.register(JapaneseFood)
admin.site.register(WesternFood)
admin.site.register(FastFood)
admin.site.register(Dessert)
admin.site.register(Drink)


