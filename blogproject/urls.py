from django.contrib import admin
from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('category/<int:category_id>',views.get_posts),
    path('apiview/',views.PostListGenericAPIView.as_view(), name="api_view"),
    path('userpost/<int:writer_id>',views.get_posts_user),
    path('usercomment/<int:writer_id>',views.get_comments_user),
    path('mypost/',views.get_my_posts),
    path('mycomment/',views.get_my_comments),
    path('new/', views.new, name = 'new'),
    path('community/', views.community, name = 'community'),
    path('mbtitest/', views.mbtitest, name = 'mbtitest'),
    path('detail/<int:post_id>', views.detail, name = 'detail'),
    path('edit/<int:post_id>', views.edit, name = 'edit'),
    path('delete/<int:post_id>', views.delete, name = 'delete'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name = 'edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name = 'delete_comment'),
    path('accounts/', include('accounts.urls',namespace='accounts')),


]
