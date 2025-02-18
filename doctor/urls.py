from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('designation/', views.DesignationViewSet)
router.register('specialization/', views.SpecializationViewSet)
router.register('available_time/', views.AvailableTimeViewSet)
router.register('list/', views.DoctorViewSet)
router.register('review/', views.ReviewerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]