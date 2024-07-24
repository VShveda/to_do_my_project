from django.urls import path
from to_do.views import index, TagListView


urlpatterns = [
    path("", index, name="index"),
    path("tegs/", TagListView.as_view(), name="tag_list"),
]