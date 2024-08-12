from os import getenv
from flask import Flask, jsonify
import math, psutil
import socket

HOSTNAME = socket.gethostname()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    target = getenv('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

@app.route('/status', methods=['GET'])
def status():
	return jsonify(
    Message = "Hello {}!".format(getenv('TARGET', 'World')),
	), 200, {'ContentType':'application/json'}

@app.route('/stress', methods=['GET'])
def stress():
    # Stress the CPU by calculating square root of a number
    x = 0.0001
    for i in range(10000000):  # Loop from 0 to 10000000
        x += math.sqrt(x)
    cpu_after = psutil.cpu_percent(interval=1)
    return jsonify(
    Message = "Stress test completed",
    Current_CPU_Usage = f"{cpu_after}%",
    Hostname = HOSTNAME
    ), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8883)
