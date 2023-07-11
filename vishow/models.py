import requests
from django.db import models
import efinance as ef
import pandas as pd

class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)  # 设置默认值为0.00

    # 其他代码...

    def update_price(self):
        try:
            # 获取实时股票行情数据
            quotes = ef.stock.get_realtime_quotes()

            # 筛选所需字段
            filtered_quotes = quotes[['股票名称']]

            # 打印结果
            print(filtered_quotes)

            self.name = filtered_quotes.iloc[0]['股票名称']
            self.price = float(filtered_quotes.iloc[0]['最新价'])
            self.save()
        except Exception as e:
            # 处理异常情况，例如输出错误信息或进行其他适当的处理
            print(f"Failed to update stock price: {e}")

    # 其他代码...
