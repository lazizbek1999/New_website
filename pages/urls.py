from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    # path('',post_list, name="post_list" )
    path('',PostList.as_view(), name="home" ),
    path('post/<int:pk>/',DetailView.as_view(), name='detail' ),
    
    
]