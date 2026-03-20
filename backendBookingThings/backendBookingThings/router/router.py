from rest_framework.routers import DefaultRouter
from resource import views
from user import views as userView

router = DefaultRouter()
router.register(r'resources', views.ResourceViewSet)
router.register(r'users', userView.UserViewSet)