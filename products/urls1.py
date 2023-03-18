from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

router = DefaultRouter()

app_name = "productlistapp"

router.register(
    prefix="product",
    viewset=ProductViewSet,
    basename="product",
)

urlpatterns = router.urls
