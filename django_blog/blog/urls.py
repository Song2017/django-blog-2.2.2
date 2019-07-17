from django.conf.urls import url
from django.urls import path
from . import views

# 视图函数命名空间: 区分不同的应用
app_name = "blog"

urlpatterns = [
    path(r"", views.IndexView.as_view(), name="index"),
    url(r"^post/(?P<pk>[0-9]+)/$",
        views.PostDetailView.as_view(),
        name="detail"),
    url(
        r"^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$",
        views.ArchivesView.as_view(),
        name="archives",
    ),
    url(r"^category/(?P<pk>[0-9]+)/$",
        views.CategoryView.as_view(),
        name="category"),
    url(r"^tag/(?P<pk>[0-9]+)/$", views.TagView.as_view(), name="tag"),
]
