from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # if not found any url match, then it will go to 404 page
    re_path(r'^.*/$', views.not_found, name="not_found"),
]
