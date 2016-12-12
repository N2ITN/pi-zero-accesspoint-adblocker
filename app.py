
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
from os import curdir, sep
import cgi

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="/app.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    #Handler for the POST requests
    def do_POST(self):
        if self.path=="/send":
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
            })

            print "Connecting to: %s" % form["network"].value
            print "Password: %s" % form["password"].value
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Connecting to: %s" % form["network"].value)
            self.network = form["network"].value
            self.passkey = form["password"].value
            try: 
                reconnect(self.network, self.passkey)
            except Exception as e:
                print e
                exit()
                
            server.socket.close()
def reconnect(network,passkey):
    os.chdir('/home/pirate/zer0')
    os.system('mv startAP.sh startAP_old.sh')
    with open('startAP.sh','w') as out:
        out.write('sudo python switch_wifi.py')# && bash pihole.sh')
    os.system('chmod +x startAP.sh')
    with open('credentials.txt','w') as out:
        out.write(' '.join([network, passkey]))
    os.system('sudo python switch_wifi.py')
    os.system('sudo reboot now')



    



try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    
