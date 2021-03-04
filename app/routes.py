from app import app
import os
import urllib.request
from flask import flash, request, redirect, render_template , Response
from werkzeug.utils import secure_filename
import sys
ALLOWED_EXTENSIONS = set(['mp4','wmv'])
@app.route('/')
def upload():
	return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/upload',methods =['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            status_code = Response(status=204)
            return status_code
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            status_code = Response(status=200)
            
            return status_code
        else:
            status_code = Response(status=406)
            return status_code
