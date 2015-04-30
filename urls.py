from django.conf.urls import include, url
from dinghuo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'flashsale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/', views.orderadd, name="orderadd"),
    # url(r'^add/',  views.add, name="addorder"),
    # url(r'^delorder/(?P<del_id>\d+)',  views.delorder, name="delorder"),
    # url(r'^update/(?P<modify_id>\d+)', views.update, name="updateorder"),
    # url(r'^login/', views.login, name="login"),
    # url(r'^logout/', views.logout, name='logout'),
    # url(r'^register/$', views.regist, name='register'),
    # url(r'^detail/(?P<detail_id>\d+)', views.detail, name='orderdetail'),
    # url(r'^addorderitem/$', views.addorderitem, name='addorderitem'),
    # url(r'^ajax_deal/$', views.ajax_index, name="test-ajax"),
    # url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^checkorderexist/$', views.CheckOrderExist, name='CheckOrderExist'),
    url(r'^searchproduct/$', views.searchProduct, name='searchProduct'),
    url(r'^initdraft/$', views.initdraft, name='initdraft'),
    url(r'^dingdan/$', views.neworder, name="adddingdan"),
    url(r'^delcaogao/$', views.delcaogao, name="delcaogao"),
    url(r'^test/$', views.test, name="test"),



]
