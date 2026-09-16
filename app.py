import logging

from flask import render_template

from setup import create_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')