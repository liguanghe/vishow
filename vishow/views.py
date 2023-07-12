from django.shortcuts import render
from .models import Stock

def home(request):
    if request.method == 'POST':
        code = request.POST.get('stock_code')
        stock = Stock.objects.create(code=code)  # 创建新的股票对象
        stock.update_price()  # 更新股票数据并创建新的记录

    stocks = Stock.objects.all()
    for stock in stocks:
        stock.update_price()  # 更新股票数据并创建新的记录

    return render(request, 'home.html', {'stocks': stocks})
