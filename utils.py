import os
import re

from bs4 import BeautifulSoup
from markdown import markdown

from config import ALLOWED_EXTENSION


def get_extension(file):
    """
    Récupère l'extension d'un fichier (sans le point), en minuscule.
    Ex: 'document.PDF' -> 'pdf'
    """
    _, ext = os.path.splitext(file)
    return ext.lstrip(".").lower()


def is_allowed(file):
    """
    Chek if file extention is allowed
    """
    return '.' in file and file.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSION


def md2txt(string):
    """
    Convertit une chaîne Markdown en texte brut.
    """
    # Source - https://stackoverflow.com/a/761847
    # Posted by Jason Coon, modified by community.
    # Retrieved 2026-09-19, License - CC BY-SA 4.0

    # ~~texte~~  noy supported by "markdown" 
    string = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', string)

    html = markdown(string)
    text = ''.join(BeautifulSoup(html, features="lxml").find_all(string=True))

    return text.strip()



