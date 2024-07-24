from django.urls import path
from to_do.views import index, TagListView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tegs/", TagListView.as_view(), name="tag_list"),
    path("teg_create/", TagCreateView.as_view(), name="tag_create"),
    path("teg_update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("teg_delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]