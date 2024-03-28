from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = { "date": today }
    return render(request, "menus/index.html", context=context)

def detail(request, food):
    context = { "food": food }
    return render(request, "menus/detail.html", context=context)
