from channels.generic.websocket import WebsocketConsumer
from datetime import datetime


class TimeConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=datetime.now().strftime("%H:%M:%S"))
