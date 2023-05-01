from rest_framework import authentication,generics, mixins

from .models import Product
from .serializers import ProductSerializer
#from ..api.permissions import IsStaffEditorPermission
#from api.authentication import TokenAuthentication
from api.mixins import IsStaffEditorPermission

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(
    IsStaffEditorPermission,
    generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication,
    #                           TokenAuthentication
    #                           ]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
 
product_list_view = ProductListAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        
product_delete_view = ProductDeleteAPIView.as_view()



class ProductMixinView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        #print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return(self.list(request, *args, **kwargs))
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.destroy(request, *args, **kwargs)
    
product_mixin_view = ProductMixinView.as_view()
