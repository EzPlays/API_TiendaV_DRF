from rest_framework import routers
from api.views import ProductsViewSet, ShoppingViewSet, ShoppingCartViewSet, UsersViewSet


router = routers.DefaultRouter()


router.register(r'products', ProductsViewSet, basename='products')
router.register(r'shopping', ShoppingViewSet, basename='shopping')
router.register(r'shoppingcart', ShoppingCartViewSet, basename='shoppingcart')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = router.urls



