from django.urls import path

from . import views
app_name = 'main'
urlpatterns = [
    path('', views.home, name="home"),
    path('blog/posts/', views.post_listing, name="post-list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail,
    name='post_detail'),
  
    path('search/', views.search_post, name="search"),
]
