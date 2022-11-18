from rest_framework import routers
from api.views import ProductsViewSet, ShoppingViewSet, ShoppingCartViewSet, UsersViewSet, UserLoginViewSet

router = routers.DefaultRouter()

router.register('products', ProductsViewSet)
router.register('shopping', ShoppingViewSet)
router.register('shoppingcart', ShoppingCartViewSet)
router.register('users', UsersViewSet)
router.register('signin', UserLoginViewSet, basename='signin')
# router.register('api/carrito', ShoppingCartViewSet, 'carrito')
# router.register('api/compras', ShoppingViewSet, 'compras')
# router.register('api/usuarios', UsersViewSet, 'usuarios')

urlpatterns = router.urls



