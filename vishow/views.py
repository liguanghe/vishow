from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock

def convert_to_trillion(number):
    if number is not None:
        return round(number / 10**12, 4)
    else:
        return None

def home(request):
    stocks = Stock.objects.all()

    # Convert the circulation market value, buy price and sell price to the form of trillion
    for stock in stocks:
        stock.market_cap = convert_to_trillion(stock.market_cap)
        stock.buy_price = convert_to_trillion(stock.buy_price)
        stock.sell_price = convert_to_trillion(stock.sell_price)

    return render(request, 'home.html', {'stocks': stocks})

def update_plan_price(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if request.method == "POST":
        buy_price = request.POST.get('buy_price')
        sell_price = request.POST.get('sell_price')
        
        # Convert the buy price and sell price to the form of trillion
        buy_price = convert_to_trillion(float(buy_price))
        sell_price = convert_to_trillion(float(sell_price))

        stock.buy_price = buy_price
        stock.sell_price = sell_price
        stock.save()

        return redirect('home')

    return render(request, 'home.html', {'stock': stock})
