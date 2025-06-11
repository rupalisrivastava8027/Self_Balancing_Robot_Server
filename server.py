from flask import Flask, render_template, jsonify, request
from Gyro import Gyro
from MotorController import MotorController

app = Flask(__name__)

sensor = Gyro()
motor = MotorController() 

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(
        {"PitchAngle": sensor.getPitchAngle(),
         "MotorSpeed": motor.getSpeed()
        })

@app.route("/requests", methods=["POST"])
def handle_POST():
    data = request.get_json()
    return jsonify({"Recieved data": data})

if (__name__ == "__main__"):
    app.run(debug=True, port=5000)