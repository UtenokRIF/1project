from django.urls import path
from .views import catalog, product_detail, create_order
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'), 
    #path('order/', order, name='order'),
    path('creater_order/', create_order, name='create_order'),
 
   

]
