from flask import Flask, request, abort
from geventwebsocket import WebSocketError
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
users = set()

@app.route('/websocket/')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    users.add(wsock)
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()  # 接收客户端发来的信息
        except WebSocketError:
            break
        print
        u"现有连接用户：%s" % (len(users))

        if message:
            for user in users:
                try:
                    user.send(message)  # 给客户端推送信息
                except WebSocketError:
                    print
                    u'用户已断开连接'
    # 如果有客户端断开，则删除这个断开的websocket
    users.remove(wsock)

if __name__ == '__main__':
    server = WSGIServer(("0.0.0.0", 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()
