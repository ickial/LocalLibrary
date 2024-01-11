from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='author_list'),
    re_path('accounts/', include('django.contrib.auth.urls')),
    ]
