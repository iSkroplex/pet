from . import views
from django.urls import path

from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add_news', views.add_news, name='add_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]
