from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('',views.allProdCategory,name='allProdCategory'),
    path('<slug:c_slug>/',views.allProdCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetail,name='prodcatdetail'),

]