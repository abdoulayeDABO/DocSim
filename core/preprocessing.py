import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer  # Fixed: Use Snowball for French
from nltk.tokenize import word_tokenize

# Fixed: Ensure modern tokenization data and stopwords are downloaded
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)


def prepare_text(text):
    """Tokenizes, filters French stopwords, and stems the input text."""
    # 1. Tokenize into individual words and punctuation marks first
    words = word_tokenize(text.lower())  # lowercasing ensures better matches

    # 2. Fetch French stop words
    stops = set(stopwords.words("french"))

    # 3. Filter out stop words and structural punctuation
    meaningful_words = []
    for word in words:
        if word not in stops and word.isalnum():  # isalnum removes pure punctuation
            meaningful_words.append(word)

    # 4. Stem the remaining words using the French stemmer
    stemmer = SnowballStemmer("french")
    stemmed_words = []
    for word in meaningful_words:
        stemmed_words.append(stemmer.stem(word))

    # 5. Rejoin into a single cleaned string
    return " ".join(stemmed_words)



