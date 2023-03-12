from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import (NewsList, CategoryList, NewsDetail,SelCatList, NewsCreate, ArticleCreate,
                    NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete, subscribe_political, subscribe_health,
                    subscribe_education, subscribe_sport)


urlpatterns = [
   path('', NewsList.as_view(), name = 'news_list'),
   path('categories/',CategoryList.as_view(), name = 'all_cat'),
   path('categories/health/',SelCatList.as_view(template_name = 'healthNews.html'), name = ''),
   path('categories/health/subscribe', subscribe_health),
   path('categories/education/',SelCatList.as_view(template_name = 'educationNews.html')),
   path('categories/education/subscribe', subscribe_education),
   path('categories/sport/',SelCatList.as_view(template_name = 'sportNews.html'), name = ''),
   path('categories/sport/subscribe', subscribe_sport),
   path('categories/politics/',SelCatList.as_view(template_name = 'politicalNews.html')),
   path('categories/politics/subscribe', subscribe_political),
   path('news/create', NewsCreate.as_view(), name = 'news_create'),
   path('article/create', ArticleCreate.as_view(), name = 'article_create'),
   path('news/<int:pk>/edit', NewsUpdate.as_view(), name = 'news_update'),
   path('article/<int:pk>/edit', ArticleUpdate.as_view(), name = 'article_update'),
   path('news/<int:pk>/delete', NewsDelete.as_view(), name = 'news_delete'),
   path('article/<int:pk>/delete', ArticleDelete.as_view(), name = 'article_delete'),
   path('<int:pk>', NewsDetail.as_view(), name = 'news_detail'),
   path('search/', NewsList.as_view(template_name="news_search.html"), name = 'news_search'),

]