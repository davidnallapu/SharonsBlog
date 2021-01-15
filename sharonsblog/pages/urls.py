from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('support', views.support, name='support'),
    path('podcasts', views.podcasts, name='podcasts'),
    path('<int:article_id>', views.article, name= 'article'),
    
]