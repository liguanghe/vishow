from django.contrib import admin
from django.urls import path
from . import views  # 导入你的视图模块

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 添加这一行
    path('update_price/<int:stock_id>/', views.update_plan_price, name='update_price'),
]
