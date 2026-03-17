from rest_framework.routers import DefaultRouter
from service import views

router = DefaultRouter()
router.register(r'services', views.ServiceViewSet)