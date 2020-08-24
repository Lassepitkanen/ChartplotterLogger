import tornado.ioloop
import tornado.web
import tornado.httpserver
import simplejson as json
import config
import threading

from ws_handler import WSHandler

class ServerApp(threading.Thread):
    def __init__(self, gpsPoller):
        threading.Thread.__init__(self)
        self.gpsp = gpsPoller
        self.schedule = tornado.ioloop.PeriodicCallback(self.send, config.serverDelay)
    
    def run(self):
        app = tornado.web.Application([
            (r"/gps", WSHandler),
        ])
        server = tornado.httpserver.HTTPServer(app)
        server.listen(8888)
        
        self.schedule.start()
        tornado.ioloop.IOLoop.instance().start()
        
    def stop(self):
        self.schedule.stop()
        tornado.ioloop.IOLoop.instance().stop()
        
    def send(self):
        if self.gpsp.fix.latitude > 0:
            message = json.dumps({"lat": self.gpsp.fix.latitude, "lng": self.gpsp.fix.longitude })
            WSHandler.sendMessage(message)
