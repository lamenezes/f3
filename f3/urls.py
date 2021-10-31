from django.conf.urls import url

from feeder.views import feed

urlpatterns = [
    url(r"^$", feed),
]
