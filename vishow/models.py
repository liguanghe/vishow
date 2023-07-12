import requests
from django.db import models
import efinance as ef
import pandas as pd
from django.utils import timezone
import datetime



class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    market_cap = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)  # 添加流通市值字段
    date = models.DateField(default=datetime.date.today)# 添加日期字段
    time = models.TimeField(default=timezone.now)  # 添加时间字段

    # 其他代码...

    def update_price(self):
        try:
            # 根据code来获取实时股票行情数据
            quotes = ef.stock.get_latest_quote(self.code)  # 修正获取实时股票行情数据的参数

            # 筛选所需字段
            filtered_quotes = quotes[['代码', '名称', '流通市值', '最新价']]  # 添加流通市值字段

            # 添加日期时间列
            filtered_quotes['日期'] = pd.Timestamp.now().date()
            filtered_quotes['时间'] = pd.Timestamp.now().time()


            if not filtered_quotes.empty:
                self.code = filtered_quotes.iloc[0]['代码']
                self.name = filtered_quotes.iloc[0]['名称']
                self.market_cap = float(filtered_quotes.iloc[0]['流通市值'])
                self.price = float(filtered_quotes.iloc[0]['最新价'])
                self.save()
            else:
                print("No quotes found for the given code.")
                self.delete()  # Delete the instance from the database
        except Exception as e:
            # 处理异常情况，例如输出错误信息或进行其他适当的处理
            print(f"Failed to update stock price: {e}")
