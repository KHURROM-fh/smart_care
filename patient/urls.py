# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register ViewSets
router = DefaultRouter()
router.register('list', views.PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutApiView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name= 'activate'),
]
