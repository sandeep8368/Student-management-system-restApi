from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import studentViewset


router = DefaultRouter()
router.register(r'studentModel', studentViewset)


urlpatterns = [
    path('rest/', include(router.urls)),
]
