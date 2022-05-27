# encoding: UTF-8
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import time
import os
from sys import platform
import pyodbc as db
import urllib.parse

hostName = "localhost"
serverPort = 8080

if platform == 'win32':
    DSNFile = os.getcwd() + "\DATASOURCENAME.dsn"
    h_connection = r'FILEDSN=' + DSNFile

elif platform == 'os400':
    h_connection = 'DSN=*LOCAL'

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Menzel's HTTP Server</title></head>", "iso-8859-1"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "iso-8859-1"))
        MyServer.prcCommand(self)
        
    def prcCommand(self):
        h_cmd = self.path.split('&')
        
        if h_cmd[0] == '/nachricht':
            h_nachricht = urllib.parse.unquote_plus(h_cmd[1])
            h_len = len(h_nachricht.strip()) + 29
            connection = db.connect(h_connection)
            c1 = connection.cursor()
            sqlStmt="call qsys2.qcmdexc('SNDMSG MSG(''{}'') TOUSR(*SYSOPR)', {})".format(h_nachricht, h_len) 
            c1.execute(sqlStmt)
            c1.connection.close()
            self.wfile.write(bytes("<body>", "iso-8859-1"))
            self.wfile.write(bytes("<p>Nachricht erfolgreich gesendet!.</p>", "iso-8859-1"))
            self.wfile.write(bytes("</body></html>", "iso-8859-1"))

        elif h_cmd[0] == '/file':
            h_filelib = urllib.parse.unquote_plus(h_cmd[1])
            connection = db.connect(h_connection)
            c1 = connection.cursor()
            sqlStmt="select * from {}".format(h_filelib)
            c1.execute(sqlStmt)
            self.wfile.write(bytes("<body>", "iso-8859-1"))
            for row in c1:
                self.wfile.write(bytes("<p>" + str(row) + "</p>", "iso-8859-1"))
            c1.connection.close()
            self.wfile.write(bytes("</body></html>", "iso-8859-1"))

        elif h_cmd[0] == '/STOP':
            self.wfile.write(bytes("<body>", "iso-8859-1"))
            self.wfile.write(bytes("<p>Server wurde beendet.</p>", "iso-8859-1"))
            self.wfile.write(bytes("</body></html>", "iso-8859-1"))
            self.wfile.flush()
            webServer.shutdown()

if __name__ == "__main__":        
    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")