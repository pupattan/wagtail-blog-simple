from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'wagtail_blog'

urlpatterns = [
    path('', views.index_page, name="index"),
    url(r'(?P<blog_slug>[\w-]+)/', views.blog_view, name="blog_view"),
    url(r'^tag/(?P<tag>[-\w]+)/', views.tag_view, name="tag"),
    url(r'^category/(?P<category>[-\w]+)/feed/$', views.LatestCategoryFeed(), name="category_feed"),
    url(r'^category/(?P<category>[-\w]+)/', views.category_view, name="category"),
    url(r'^author/(?P<author>[-\w]+)/', views.author_view, name="author"),
    url(r'(?P<blog_slug>[\w-]+)/rss.*/',
        views.LatestEntriesFeed(),
        name="latest_entries_feed"),
    url(r'(?P<blog_slug>[\w-]+)/atom.*/',
        views.LatestEntriesFeedAtom(),
        name="latest_entries_feed_atom"),
]
