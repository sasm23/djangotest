from django.urls import path

from . import views

urlpatterns = [
    path('',views.product_create_view),
    #path('',views.product_mixin_view),
    #<use mixin view>
    path('get/',views.product_list_view, name='products-list'),
    #path('get/',views.product_mixin_view),
    #path('<int:pk>/update/',views.product_update_view),
    path('<int:pk>/update/',views.product_mixin_view, name= 'update_view'),
    #path('<int:pk>/delete/',views.product_delete_view),
    path('<int:pk>/delete/',views.product_mixin_view),
    path('<int:pk>/',views.product_detail_view, name='detail_view')
    #path('<int:pk>/',views.product_mixin_view)
]