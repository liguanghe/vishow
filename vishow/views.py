from django.shortcuts import render
from .models import Stock

def home(request):
    if request.method == 'POST':
        code = request.POST.get('stock_code')
        stock, created = Stock.objects.get_or_create(code=code)
        if created:
            stock.update_price()

    stocks = Stock.objects.all()
    for stock in stocks:
        stock.update_price()

    return render(request, 'home.html', {'stocks': stocks})
