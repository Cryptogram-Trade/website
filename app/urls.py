from django.contrib import admin
from django.urls import path, include

from views import (
    HomeView,
    BlogView,
    PageView,
    SupportView,
    SiteMapView,
    RobotsView
)

urlpatterns = [
    path(
        route='',
        view=HomeView.as_view(),
        name="home"
    ),
    path(
        route='blog/<slug>',
        view=BlogView.as_view(),
        name="blog"
    ),
    path(
        route='page/<slug>',
        view=PageView.as_view(),
        name="page"
    ),
    path(
        route='support/',
        view=SupportView.as_view(),
        name="support"
    ),
    path(
        route='sitemap.xml',
        view=SiteMapView.as_view(),
        name="sitemap"
    ),
    path(
        route='robots.txt',
        view=RobotsView.as_view(),
        name="robots"
    ),
    path(
        route="users/",
        view=include(
            ('users.urls', 'users'),
            namespace="users"
        )
    ),
    path(
        route='stripe/',
        view=include(
            "djstripe.urls",
            namespace="djstripe"
        ),
    ),
    path(
        route='auth/',
        view=include('allauth.urls')
    ),
    path(
        route='admin/',
        view=admin.site.urls,
    ),
]
