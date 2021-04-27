from django.urls import path

from .views import (
    ListView,
    ArticleView,
)

urlpatterns = [
    path(
        route='',
        view=ListView.as_view(),
        name="list"
    ),
    path(
        route='<slug>',
        view=ArticleView.as_view(),
        name="article"
    ),
]
