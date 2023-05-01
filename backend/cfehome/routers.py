from rest_framework.routers import DefaultRouter

#from products.viewsets import ProductViewSet
from products.viewsets import ProductGenericViewSet
router = DefaultRouter()
#router.register('products-abc', ProductViewSet, basename='products')
router.register('product-ab',ProductGenericViewSet, basename='productss')
urlpatterns = router.urls