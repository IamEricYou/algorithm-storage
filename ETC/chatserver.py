import gevent
from redis import Redis
from geventwebsocket.resource import Resource, WebSocketApplication
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import uuid
import logging
import json
from gevent import monkey
monkey.patch_all()


class MemoryBroker():
    def __init__(self):
        self.sockets = {}

    def subscribe(self, key, socket):
        if key not in self.sockets:
            self.sockets[key] = set()

        if socket in self.sockets[key]:
            return

        self.sockets[key].add(socket)

    def publish(self, key, data):
        for socket in self.sockets[key]:
            socket.on_broadcast(data)

    def unsubscribe(self, key, socket):
        if key not in self.sockets:
            return

        self.sockets[key].remove(socket)


class RedisMemoryBroker():
    def __init__(self):
        self.sockets = {}
        self.red = Redis(host=u'localhost', port=6379)
        self.pubsub = self.red.pubsub()

    def subscribe(self, key, socket):
        userid = socket.userid.hex

        if key not in self.sockets:
            self.sockets[key] = dict()

        if userid in self.sockets[key]:
            return

        self.pubsub.subscribe([key])
        gevent.spawn(self.handler, key, socket, self.pubsub)

    def handler(self, key, socket, pubsub):
        userid = socket.userid.hex
        self.sockets[key][userid] = self.pubsub
        for connection in self.pubsub.listen():
            print(connection)
            if connection['type'] == 'message':
                data = json.loads(connection['data'])
                socket.on_broadcast(data)

    def publish(self, key, data):
        self.red.publish(key, json.dumps(data))

    def unsubscribe(self, key, socket):
        if key not in self.sockets:
            return

        self.pubsub.unsubscribe()


broker = RedisMemoryBroker()


class Chat(WebSocketApplication):

    def on_open(self, *args, **kwargs):
        self.userid = uuid.uuid4()
        broker.subscribe('room1', self)

    def on_close(self, *args, **kwargs):
        broker.unsubscribe('room1', self)

    def on_message(self, message, *args, **kwargs):
        if not message:
            return

        data = json.loads(message)
        data['user'] = self.userid.hex
        broker.publish('room1', data)

    def on_broadcast(self, data):
        self.ws.send(json.dumps(data))


def index(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    html = open('index.html', 'rb').read()
    return [html]


application = Resource([
    ('^/chat', Chat),
    ('^/', index)
])


if __name__ == '__main__':
    print("Server is running on .... /8000")
    WSGIServer('{}:{}'.format('0.0.0.0', 8000), application,
               handler_class=WebSocketHandler).serve_forever()
