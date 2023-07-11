import requests
from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)  # 设置默认值为0.00

    # 其他代码...

    def update_price(self):
        try:
            url = f"http://hq.sinajs.cn/list={self.code}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text
                # 解析股票数据并更新价格
                # 这里需要根据新浪股票数据接口的返回格式进行解析
                # 假设数据格式为：var hq_str_sh601006="大秦铁路,9.04,9.08,...";
                parsed_data = data.split("=")[1].strip('";')
                stock_info = parsed_data.split(",")
                if len(stock_info) >= 2:
                    self.name = stock_info[0]
                    self.price = float(stock_info[1])
                    self.save()
        except Exception as e:
            # 处理异常情况，例如输出错误信息或进行其他适当的处理
            print(f"Failed to update stock price: {e}")

    # 其他代码...
