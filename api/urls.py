from rest_framework import routers
from .views import BlogViewsets
from django.urls import path,include



router = routers.DefaultRouter()

router.register('blog', BlogViewsets, basename='blog')

urlpatterns = router.urls