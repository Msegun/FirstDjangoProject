from django.conf.urls import url

from . import consumer

websocket_urlpatterns = [
    url(r'^ws/authorTime/$', consumer.TimeConsumer),
]