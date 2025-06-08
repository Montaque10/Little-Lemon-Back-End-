from django.contrib import admin 
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')
router.register(r'menus', views.MenuViewSet, basename='menu')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [ 
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/categories/', views.CategoriesView.as_view()),
    path('api/menu-items/', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('api/message/', views.msg),
    path('api/api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]