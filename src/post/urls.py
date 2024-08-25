from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView
from .views import LikeView
urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail' ),
    path('add_post/', AddPostView.as_view(), name = 'add_post' ),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name = 'update_post' ),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name = 'delete_post' ),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),

]