from django.urls import path
from . import views
# Vistas genericas creadas
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostView
)

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    # se nombra por default post_detail 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    # la ruta para los posts del usuario
    path('user/<str:username>/', UserPostView.as_view(), name='user-posts')

    
]