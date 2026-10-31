from django.urls import path
from .views import PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'pages'

urlpatterns = [
    path('',PostList.as_view(), name="home" ),
    path('post/<int:pk>/',PostDetail.as_view(), name='post-detail' ),
    path('post/new/', PostCreateView.as_view(), name="post-new"),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    
]