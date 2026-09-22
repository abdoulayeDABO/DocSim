from utils import is_allowed, md2txt


def test_file_not_alllowed():
    file = "file2.r"
    assert is_allowed(file) == False
    

def test_file_extension_ok():
    file = "file1.pdf"
    assert is_allowed(file) == True
    
    
def test_md2txt():
    md_str = """# Titre de niveau 1
Voici un paragraphe standard. Vous pouvez facilement appliquer du style au texte :
* Ce texte est en **gras** (ou avec des __double underscore__).
* Ce texte est en *italique* (ou avec des _single underscore_).
* Il est aussi possible de combiner du **_gras et de l'italique_**.
* Vous pouvez également ~~barrer du texte~~.
"""
    cleaned_str = md2txt(md_str)
    
    # Aucun symbole Markdown ne doit subsister
    assert '#' not in cleaned_str
    assert '**' not in cleaned_str
    assert '__' not in cleaned_str
    assert '~~' not in cleaned_str
    assert '`' not in cleaned_str

    # Le contenu textuel doit être préservé
    assert "Titre de niveau 1" in cleaned_str
    assert "gras" in cleaned_str
    assert "italique" in cleaned_str
    assert "double underscore" in cleaned_str
    assert "single underscore" in cleaned_str
    assert "barrer du texte" in cleaned_str
  