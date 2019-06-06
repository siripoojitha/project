from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from flask import Flask, render_template, \
    send_from_directory, request, Response, redirect, url_for
import jsonpickle
import json
import os
import sys
from absl import flags
import numpy as np
from werkzeug import secure_filename
import skimage.io as io
import tensorflow as tf
# from src.util import renderer as vis_util
sys.path.insert(0, './hmr/')
import src.config
from demo import preprocess_image, get_model
model = None

app = Flask(__name__, static_url_path='')
@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/static/js', path)

@app.route('/upload_data/<path:path>')
def send_upload_data(path):
    return send_from_directory('upload_data', path)

@app.route('/display/<path:path>')
def index_w_path(path):
    fileList = get_upload_image()
    render_obj = render(path)
    return render_template('index.html', fileList=fileList, render=render_obj)

@app.route('/')
def index():
    fileList = get_upload_image()
    render_obj = render('random.jpg')
    return render_template('index.html', fileList=fileList, render=render_obj)

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
            if '.jpg' in f or '.png' in f:
                fileList.append(f)
    print('current files: ')
    print(fileList)
    return fileList

default_shape = {}
def render(path):
    input_img, proc_param, img = preprocess_image('./upload_data/'+path)
    input_img = np.expand_dims(input_img, 0)
    joints, verts, cams, joints3d, theta = model.predict( input_img, get_theta=True)
    return {
        'imageLink': path.encode("utf-8"),
        'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0]),
        'verts': verts[0].tolist(),
    }

if __name__ == "__main__":
    # start flask app
    path = './models/'
    model = get_model(path)
    app.run(host="0.0.0.0", port=5000)    