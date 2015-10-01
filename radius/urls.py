from django.conf.urls import patterns, url

from radius.views import RadiusAPI

urlpatterns = patterns(
    '',
    url(r'^$', RadiusAPI.as_view()),
)
