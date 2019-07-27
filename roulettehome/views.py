from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import KoreanFood, ChineseFood, JapaneseFood, WesternFood, FastFood, Dessert, Drink

# Create your views here.
def home(request):
    return render(request,'home.html')