from pypdf import PdfReader

from utils import md2txt


def extrac_from_raw_text(file):
    """
    this function extrac text from raw file passed as parameter.
    """
    with open(file, "r") as f:
        return f.read()


def extrac_from_pdf(file):
    """
    this function extrac text from pdf file passed as parameter.
    """
    file_content = []
    reader = PdfReader(file)
    for page in reader.pages:
        page_text = page.extract_text(0)
        file_content.append(page_text) 

    return " ".join(file_content)


def extrac_from_md(file):
    """
    this function extrac text from md file passed as parameter.
    """
    with open(file, "r") as f:
        file_content = f.read()
        file_content = md2txt(file_content)

    return file_content


def extract_text(file, type=None):
    """
    Dispatch vers la bonne fonction d'extraction selon le type de fichier.
    """
    
    match type:
        case "pdf":
            return extrac_from_pdf(file)
        case "md" | "markdown":
            return extrac_from_md(file)
        case "txt" | "text":
            return extrac_from_raw_text(file)
        case _:
            raise ValueError(f"Type de fichier non supporté: '{type}'")