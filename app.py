import logging
import os

from flask import jsonify, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

from config import MAX_FILE_SIZE
from core.extractor import extract_text
from core.preprocessing import prepare_text
from core.similarity import cosine_score
from setup import create_app
from utils import get_extension, is_allowed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()
CORS(app)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify(error="Le fichier est trop volumineux (Max 16 Mo)"), 413


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        uploaded_files = list(request.files.values())

        if len(uploaded_files) == 0:
            return jsonify({"error": "Aucun fichier reçu."}), 400

        if len(uploaded_files) != 2:
            return jsonify({"error": "Veuillez envoyer exactement 2 fichiers."}), 400

        # chek extension
        for file in uploaded_files:
            if not is_allowed(file.filename):
                return jsonify({"error": "Type de fichier non autorisé."}), 400

        # save files
        # for file in uploaded_files:
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        # check similarity
        file1 = uploaded_files[0]
        file2 = uploaded_files[1]
        
        try:
            file1_str = extract_text(file1, get_extension(file1.filename))
            file2_str = extract_text(file2, get_extension(file2.filename))
    
            file1_str = prepare_text(file1_str)
            file2_str = prepare_text(file2_str)
            
            score = cosine_score(file1_str, file2_str )
            return jsonify({"score": float(score)}), 200
        
        except  Exception as e:
            print(e)
            return jsonify({"error": "An error occured."}), 500
        
        
        
            
    return jsonify(message="succes" , status=200), 200