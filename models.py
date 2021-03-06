# -*- coding:utf-8 -*-
from django.db import models
from shopback.archives.models import Supplier

class OrderList(models.Model):
    orderlistID = models.CharField(primary_key=True, max_length=10, verbose_name=u"订单编号")  # 订单编号
    buyer_name = models.CharField(max_length=32, verbose_name=u'买手')
    order_amount = models.FloatField(default=0, verbose_name=u'金额')
    supplier_name = models.CharField(max_length=128, verbose_name=u'供应商')
    # supplier_name = models.ForeignKey(Supplier, verbose_name=u'供应商')
    express_company = models.CharField(default="", max_length=32, verbose_name=u'快递公司')
    express_no = models.CharField(default="", max_length=32, verbose_name=u'快递单号')
    receiver = models.CharField(max_length=32, verbose_name=u'仓库负责人')
    status = models.CharField(max_length=32, verbose_name=u'订货单状态')
    created = models.DateField(verbose_name=u'订货日期')
    updated = models.DateField(auto_now_add=True, verbose_name=u'更新日期')
    note = models.TextField(verbose_name=u'备注信息')

    class Meta:
        db_table = 'suplychain_flashsale_orderlist'
        verbose_name = u'订货表'
        verbose_name_plural = u'订货表'

    def __unicode__(self):
        return self.orderlistID


class OrderDetail(models.Model):
    orderlistID = models.ForeignKey(OrderList, verbose_name=u'订单编号')
    product_id = models.CharField(max_length=32, verbose_name=u'产品编码')
    product_name = models.CharField(max_length=128, verbose_name=u'产品名称')
    product_chicun = models.CharField(max_length=100, verbose_name=u'产品尺寸')
    buy_quantity = models.IntegerField(verbose_name=u'产品数量')
    arrival_quantity = models.IntegerField(default=0, verbose_name=u'到货数量')
    created = models.DateField(verbose_name=u'生成日期')
    updated = models.DateField(verbose_name=u'更新日期')


    class Meta:
        db_table = 'suplychain_flashsale_orderdetail'
        verbose_name = u'订货明细表'
        verbose_name_plural = u'订货明细表'

    def __unicode__(self):
        return self.product_id

class orderdraft(models.Model):
    buyer_name = models.CharField(max_length=32, verbose_name=u'买手')
    product_id = models.CharField(max_length=32, verbose_name=u'产品编码')
    product_name = models.CharField(max_length=128, verbose_name=u'产品名称')
    product_chicun = models.CharField(default="", max_length=20, verbose_name=u'产品尺寸')
    buy_unitprice = models.FloatField(verbose_name=u'买入价格')
    buy_quantity = models.IntegerField(verbose_name=u'产品数量')
    created = models.DateField(auto_now_add=True, verbose_name=u'生成日期')

    class Meta:
        db_table = 'suplychain_flashsale_orderdraft'
        verbose_name = u'草稿表'
        verbose_name_plural = u'草稿表'

    def __unicode__(self):
        return self.product_name