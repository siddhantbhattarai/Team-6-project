from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post-list',views.post_list,name="post_list"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
]
