import os

from flask import Flask, request, render_template, Response
from werkzeug import secure_filename
from videocamera import VideoCamera
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
#运行前先打开摄像头
camera_intance = VideoCamera()

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

    return Response(gen(),
             mimetype='multipart/x-mixed-replace; boundary=frame')
def gen():
    while True:
        frame=camera_intance.get_frame()
        yield (b'--framern'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
