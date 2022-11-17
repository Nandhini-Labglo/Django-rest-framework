from django.urls import path,include
from .views import (
    TodoListApiView,
    TodoDetailApiView,
    ExampleView,
    CustomAuthToken,
    RegisterAPI,
    LoginAPI,
    UserViewSet,
    #RegisterUserupdateAPIView,
    
)

from todo_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippet', views.SnippetViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'brand', views.BrandViewSet)
urlpatterns = [

    path('', views.api_root),
    path('api/login/', LoginAPI.as_view()),
   
    path('api/register/',RegisterAPI.as_view()),
    #path('register/<int:pk>/',RegisterUserupdateAPIView.as_view()),

    path('auth', ExampleView.as_view()),

    path('api-token-auth/', CustomAuthToken.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('snippetslist/', views.SnippetList.as_view()),
    path('snippetslist/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippetslist/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

    #path('snippets-list/', views.snippet_list, name='snippet-list'),
    #path('snippets-list/<int:pk>/', views.snippet_detail, name='snippet-detail'),

    path('Todolist/', TodoListApiView.as_view()),
    path('Tododetail/<int:todo_id>/', TodoDetailApiView.as_view()),
    
    path('api/', include(router.urls)),

    path('Productlist/', views.ProductList.as_view()),
    path('Productlist/<int:pk>/', views.ProductDetail.as_view()),
    path('Brandlist/', views.BrandList.as_view()),
    path('Brandlist/<int:pk>/', views.BrandDetail.as_view()),

    path('parser/', ExampleView.as_view()),
]

urlpatterns += (router.urls)
