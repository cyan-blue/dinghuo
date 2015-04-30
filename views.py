# coding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core import serializers
from shopback.items.models import Product
from dinghuo.models import orderdraft, OrderDetail, OrderList
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json, datetime
from django.views.decorators.csrf import csrf_exempt


def orderadd(request):
    user = request.user
    orderDr = orderdraft.objects.all().filter(buyer_name=user)

    return render_to_response('dinghuo/orderadd.html', {"orderdraft": orderDr})


def searchProduct(request):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    ProductIDFrompage = request.GET.get("searchtext", "")
    print "ProductIDFrompage", ProductIDFrompage
    productRestult = Product.objects.filter(outer_id__icontains=ProductIDFrompage)
    # data = serializers.serialize("json", productRestult)
    # print "tttttttttttttt", data
    product_list = []
    for product in productRestult:
        product_dict = model_to_dict(product)
        product_dict['prod_skus'] = []

        guiges = product.prod_skus.all()
        for guige in guiges:
            sku_dict = model_to_dict(guige)
            product_dict['prod_skus'].append(sku_dict)

        product_list.append(product_dict)

    data = json.dumps(product_list, cls=DjangoJSONEncoder)


    # productRestult[0].prod_skus.all()

    # model_to_dict(productRestult[0])
    return HttpResponse(data)


def initdraft(request):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    tb_outer_id = request.GET.get("tb_outer_id", "")
    buy_quantity = request.GET.get("buy_quantity", "0")

    tb_sku_name = request.GET.get("tb_sku_name", "")
    buy_unitprice = request.GET.get("but_unit_price", "")
    user = request.user
    try:
        productRestult = Product.objects.get(outer_id=tb_outer_id)
    except Exception as e:
        print e
    draftqueryset = orderdraft.objects.filter(product_id=tb_outer_id, product_chicun=tb_sku_name)
    if draftqueryset:
        draftqueryset[0].buy_quantity = draftqueryset[0].buy_quantity + int(buy_quantity)
        draftqueryset[0].save()
    else:
        try:
            shijian = datetime.datetime.now()
            oDraft = orderdraft(buyer_name=user, product_id=tb_outer_id, buy_quantity=int(buy_quantity),
                                product_name=productRestult.name, buy_unitprice=float(buy_unitprice),
                                product_chicun=tb_sku_name, created=shijian)

            oDraft.save()
        except Exception as e:
            print e
    orderDrAll = orderdraft.objects.all().filter(buyer_name=user)
    data = serializers.serialize("json", orderDrAll)
    return HttpResponse(data)


@csrf_exempt
def neworder(request):
    username = request.user
    orderDrAll = orderdraft.objects.all().filter(buyer_name=username)
    print "hi", request.method == 'POST'
    if request.method == 'POST':
        amount = calamount(username)
        print amount
        post = request.POST
        shijian = datetime.datetime.now()
        orderlistID = post['orderID']
        receiver = post['consigneeName']
        supplierId = post['supplierId']
        storehouseId = post['storehouseId']
        express_company = post['express_company']
        express_no = post['express_no']
        businessDate = datetime.datetime.now()
        remarks = post['remarks']
        orderlist = OrderList.objects.get_or_create(buyer_name=username, orderlistID=orderlistID, receiver=receiver,
                                        express_company=express_company, express_no=express_no,
                                        supplier_name=supplierId, created=businessDate, updated=businessDate,
                                        note=remarks, status="提交中", order_amount=amount)
        drafts = orderdraft.objects.filter(buyer_name=username)
        for draft in drafts:
            OrderDetail.objects.get_or_create(orderlistID_id=orderlistID, product_id=draft.product_id,
                                              product_name=draft.product_name, product_chicun=draft.product_chicun,
                                              buy_quantity=draft.buy_quantity, created=shijian, updated=shijian)
        drafts.delete()
        return HttpResponseRedirect("/dinghuo/add")
    else:
        print "else"
    return render_to_response('dinghuo/shengchengorder.html', {"orderdraft": orderDrAll})


def calamount(u):
    print "fdfd", u
    amount = 0;
    drafts = orderdraft.objects.all().filter(buyer_name=u)
    print drafts
    try:
        for draft in drafts:
            print "test"
            amount = amount + draft.buy_unitprice * draft.buy_quantity
    except Exception as e:
        print e
    return amount

def CheckOrderExist(request):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    orderIDFrompage = request.GET.get("orderID", "")
    orderM = OrderList.objects.filter(orderlistID=orderIDFrompage)
    if orderM:
        result = """{"result":true}"""
    else:
        result = """{"result":false}"""
    return HttpResponse(result)

def delcaogao(request):
    username = request.user
    drafts = orderdraft.objects.filter(buyer_name=username)
    drafts.delete()
    return HttpResponse("")

def test(req):
    return render_to_response("dinghuo/testJsonto.html")