from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.utils import ScanAnalyzer

main = Blueprint('main', __name__)
analyzer = ScanAnalyzer()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Analyze the scan
        result = analyzer.analyze_scan(filepath)
        
        if result['success']:
            return jsonify({
                'message': 'Analysis complete',
                'filename': filename,
                'prediction': result['prediction'],
                'confidence': result['confidence']
            })
        else:
            return jsonify({'error': result['error']}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400 