from django.contrib import admin
from dinghuo.models import OrderList, OrderDetail, orderdraft


admin.site.register(OrderList)
admin.site.register(OrderDetail)
admin.site.register(orderdraft)

