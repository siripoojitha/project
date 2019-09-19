from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from flask import Flask, render_template, \
<<<<<<< HEAD
    send_from_directory, request, Response, redirect, url_for, json
=======
    send_from_directory, request, Response, redirect, url_for
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
import jsonpickle
import json
import os
import sys
import numpy as np
from werkzeug import secure_filename
<<<<<<< HEAD
from image_contour import detect_reference_object
sys.path.insert(0, './hmr/')
import src.config
from demo import preprocess_image, get_model
import time
=======
# from src.util import renderer as vis_util
sys.path.insert(0, './hmr/')
import src.config
from demo import preprocess_image, get_model
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
model = None

app = Flask(__name__, static_url_path='')
app.config.update( TEMPLATES_AUTO_RELOAD=True )

<<<<<<< HEAD
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('templates/static/', path)
=======
@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/static/js', path)
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/static/css', path)

@app.route('/upload_data/<path:path>')
def send_upload_data(path):
    return send_from_directory('upload_data', path)

@app.route('/display/<path:path>')
def index_w_path(path):
    fileList = get_upload_image()
    render_obj = render(path)
<<<<<<< HEAD
    timestamp = time.time()
    return render_template('index.html', fileList=fileList, render=render_obj, timestamp=timestamp)
=======
    return render_template('index.html', fileList=fileList, render=render_obj)
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be

@app.route('/')
def index():
    fileList = get_upload_image()
<<<<<<< HEAD
    render_obj = render('webcam.png')
    timestamp = time.time()
    return render_template('index.html', fileList=fileList, render=render_obj, timestamp=timestamp)

@app.route('/store')
def store():
    timestamp = time.time()
    return render_template('store.html', timestamp=timestamp)
=======
    render_obj = render('random.jpg')
    return render_template('index.html', fileList=fileList, render=render_obj)
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be

@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['file']
    filename = f.filename
    filename = secure_filename(filename)
    f.save('./upload_data/' + filename)
    return redirect(url_for('index'))

def get_upload_image():
    fileList = []
    for r, d, fs in os.walk('upload_data'):
        for f in fs:
<<<<<<< HEAD
            if '.jpeg' in f or '.png' in f:
=======
            if '.jpg' in f or '.png' in f:
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
                fileList.append(f)
    print('current files: ')
    print(fileList)
    return fileList

default_shape = {}
def render(path):
    input_img, proc_param, img = preprocess_image('./upload_data/'+path)
    input_img = np.expand_dims(input_img, 0)
    joints, verts, cams, joints3d, theta = model.predict( input_img, get_theta=True)
<<<<<<< HEAD
    joints_names = [    'Ankle',
                        'Knee',
                        'Hip.Right',
                        'Hip.Left',
                        'Knee.Left', 
                        'Ankle.Left',
                        'Wrist.Right', 
                        'Elbow.Right', 
                        'Shoulder.Right', 
                        'Shoulder.Left',
                        'Elbow.Left',
                        'Wrist.Left', 
                        'Neck', 
                        'Head', 
                        'Nose', 
                        'Eye.Left', 
                        'Eye.Right', 
                        'Ear.Left', 
                        'Ear.Right' ]
    joints_points = list(zip( joints_names, joints3d[0].tolist() )) 
    joints_points_2d = list(zip( joints_names, joints[0].tolist() )) 
    shoulder_left = joints[0][8]
    shoulder_right = joints[0][9]
    print([shoulder_left, shoulder_right])
    im = input_img[0]
    shouder_distance = detect_reference_object(None, path, './upload_data/', shoulder_left, shoulder_right)
    L = 28
    S = 19
    if shouder_distance > S and shouder_distance < L:
        cloth_size = 'M' 
    elif shouder_distance >= L:
        cloth_size = 'L'
    else: 
        cloth_size = 'S'
=======
    print(cams[0])
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
    return {
        'imageLink': path.encode("utf-8"),
        'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0]),
        'verts': verts[0].tolist(),
<<<<<<< HEAD
        'camera': cams[0].tolist(),
        'joints_points': joints_points,    
        'joints_points_2d': joints_points_2d,    
        'shouder_distance': int(shouder_distance),
        'cloth_size': cloth_size
=======
        'camera': cams[0].tolist()
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
    }

if __name__ == "__main__":
    # start flask app
    path = './models/'
    model = get_model(path)
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000, debug=True)    
=======
    app.run(host="0.0.0.0", port=5000)    
>>>>>>> 1f290a6cde9a25288e2a1ee57e9e19814cb4b8be
