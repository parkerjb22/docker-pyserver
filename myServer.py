#!/bin/bash
from flask import Flask, jsonify, request, json, render_template, send_from_directory
import picamera

FILENAME = 'image_001.jpg'
camera = picamera.PiCamera()

app = Flask(__name__)

@app.route('/info')
def info():
  return "hello"

@app.route('/pic')
def pic():
  FILENAME = 'image_001.jpg'
  camera.capture(FILENAME)
  return send_from_directory('.', FILENAME)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8082)
