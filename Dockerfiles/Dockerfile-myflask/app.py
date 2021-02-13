import socket
from flask import Flask

def getIP():
	hostname = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	print(ip)
	s.close()
	return hostname,ip
	
app = Flask(__name__)
@app.route("/")
def hello():
    hostname,ip = getIP()
    out = "Hello from hostname: " + hostname + " with host ip: " + ip
    return out
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
	