# -*- coding: utf-8 -*-

import os

from flask import Flask, request, render_template, Response
from werkzeug import secure_filename
from videocamera import VideoCamera
from videocontrol import VideoCtrl
UPLOAD_FOLDER = './'
# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        f.save(UPLOAD_FOLDER + fname)
        return "Upload OK!"
    return render_template('upload.html')


@app.route('/play')
def play():
    ctrl = VideoCtrl()
    ans = Response(gen(ctrl),
             mimetype='multipart/x-mixed-replace; boundary=frame')
    return ans

def gen(ctrl):
    # 运行前先打开摄像头
    camera_intance = VideoCamera()
    while ctrl.get_status():
        frame=camera_intance.get_frame()
        yield (b'--framern'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    return
