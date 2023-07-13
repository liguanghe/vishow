from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock

def home(request):
    if request.method == 'POST':
        code = request.POST.get('stock_code')
        stock = Stock.objects.create(code=code)  # 创建新的股票对象
        stock.update_price()  # 更新股票数据并创建新的记录
        stock = Stock.objects.get(id=stock.id)  # 重新从数据库中获取股票对象

    stocks = Stock.objects.all()
    for stock in stocks:
        assert stock.id is not None, f"Stock object has no id: {stock}"
        stock.update_price()  # 更新股票数据并创建新的记录
        stock = Stock.objects.get(id=stock.id)  # 重新从数据库中获取股票对象

    return render(request, 'home.html', {'stocks': stocks})



def update_plan_price(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        new_buy_price = request.POST.get('buy_price')
        new_sell_price = request.POST.get('sell_price')
        if new_buy_price:
            stock.buy_price = new_buy_price
        if new_sell_price:
            stock.sell_price = new_sell_price
        stock.save()
    return redirect('home')
