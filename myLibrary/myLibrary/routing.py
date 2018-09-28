# myLibrary/o
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Authors.routing

# Nie wiem dlaczego przy authors pokazuje bład ale działa

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Authors.routing.websocket_urlpatterns
        )
    ),
})