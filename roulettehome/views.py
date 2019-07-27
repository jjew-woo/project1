from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import KoreanFood, ChineseFood, JapaneseFood, WesternFood, FastFood, Dessert, Drink

# Create your views here.
def home(request):
    return render(request,'home.html')

def bestmenu(request):
    # 해당 메뉴들 객체 생성
    koreanFoods = KoreanFood.objects
    chineseFoods = ChineseFood.objects
    japaneseFoods = JapaneseFood.objects
    westernFoods = WesternFood.objects
    fastFoods = FastFood.objects
    desserts = Dessert.objects
    drinks = Drink.objects

    return render(request,'bestmenu.html',{'koreanFoods':koreanFoods,'chineseFoods':chineseFoods,'japanesFoods':japaneseFoods,
                            'westernFoods':westernFoods,'fastFoods':fastFoods,'desserts':desserts,'drinks':drinks})

def tasteboard(request):
    return render(request,'tasteboard.html')

def areaboard(request):
    check_food = ''
    if request.method == 'POST':
        check_values = request.POST.getlist('menu')
        check_food = check_values
        return render(request,'areaboard.html',{'foods':check_food})
    else:
        return render(request,'areaboard.html',{'foods':check_food})
    #return render(request,'areaboard.html')

# 홈에서 체크박스 클릭 반응
def home(request):
    check_food = ''
    if request.method == 'POST':
        check_values = request.POST.getlist('menu')
        check_food = check_values
        #if koreanFood:
        #    food = 'Korean'
        return render(request,'home.html',{'food':check_food})
        #return redirect('home')
    else:
        return render(request,'home.html',{'food':check_food})    

def new_koreanFood(request):
    return render(request, 'new_koreanFood.html')

def detail_koreanFood(request, koreanFood_id):
    koreanFoodss = get_object_or_404(KoreanFood, pk=koreanFood_id)
    return render(request, 'detail_koreanFood.html',{'koreanFood':koreanFoodss})

def create_koreanFood(request):
    koreanFood = KoreanFood()
    koreanFood.title = request.GET['title']
    koreanFood.body = request.GET['body']
    koreanFood.pub_date = timezone.datetime.now()
    koreanFood.star = request.GET['star']
    koreanFood.save()

    return render(request, 'bestmenu.html')