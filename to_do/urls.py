from django.urls import path
from to_do.views import index, TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tegs/", TagListView.as_view(), name="tag_list"),
    path("teg_create/", TagCreateView.as_view(), name="tag_create"),
    path("teg_update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("teg_delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("task_create/", TaskCreateView.as_view(), name="task_create"),
    path("task_update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task_delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]