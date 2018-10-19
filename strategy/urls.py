
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name = "strategy"
urlpatterns = [
    # 姜楠部分
    # 游记展示
    url(r'show/', views.show, name="show"),
    # 编写游记
    url(r'edit/', views.edit, name="edit"),
    # text:存数据
    url(r'addtext/', views.addtext, name='addtext'),
    url('insertdetail/', views.insertdetail, name="insertdetail"),

    # 初始部分
    # path('admin/', admin.site.urls),
    url('searchbyuserid/(?P<userid>\w+)/$', views.searchbyuserid, name="searchbyuserid"),
    url('insertdetail/', views.insertdetail, name="insertdetail"),

]
