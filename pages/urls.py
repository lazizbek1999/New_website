from django.urls import path
from .views import PostList, PostDetail

app_name = 'pages'

urlpatterns = [
    path('',PostList.as_view(), name="home" ),
    path('post/<int:pk>/',PostDetail.as_view(), name='post_detail' ),
    
    
]