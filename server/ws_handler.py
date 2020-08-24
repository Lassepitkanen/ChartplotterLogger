import tornado.websocket
import tornado.ioloop

class WSHandler(tornado.websocket.WebSocketHandler):
    live_ws = []
    def open(self):
        WSHandler.live_ws.append(self)
        
    def on_close(self):
        WSHandler.live_ws.remove(self)
        print ("WS closed")
        
    @classmethod
    def sendMessage(cls, message):
        for ws in cls.live_ws:
            if ws.ws_connection and ws.ws_connection.stream.socket:
                ws.write_message(message)
    
    def check_origin(self, origin):
        return True