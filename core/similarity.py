
import math

from gensim import corpora, matutils, models
from gensim.utils import simple_preprocess

# def cosine_score(doc1, doc2):
    
#     tokens1 = simple_preprocess(doc1)
#     tokens2 = simple_preprocess(doc2)
    
#     if not tokens1 or not tokens2:
#         return 0.0
    
#     # print(tokens1, tokens2)

#     dictionary = corpora.Dictionary([tokens1, tokens2])

#     bow_doc1 = dictionary.doc2bow(tokens1)
#     bow_doc2 = dictionary.doc2bow(tokens2)
#     corpus_bow = [bow_doc1, bow_doc2]

#     tfidf_model = models.TfidfModel(corpus_bow)
#     tfidf_doc1 = tfidf_model[bow_doc1]
#     tfidf_doc2 = tfidf_model[bow_doc2]

#     index = similarities.SparseMatrixSimilarity([tfidf_doc1], num_features=len(dictionary))
#     score = index[tfidf_doc2][0]
#     return score


def smooth_idf(docfreq, totaldocs):
    """Smoothed IDF to avoid idf=0"""
    return math.log2((1 + totaldocs) / (1 + docfreq)) + 1


def cosine_score(doc1, doc2):
    
    norm1 = " ".join(doc1.split())
    norm2 = " ".join(doc2.split())

    if norm1 == norm2:
        return 1.0


    tokens1 = simple_preprocess(doc1)
    tokens2 = simple_preprocess(doc2)

    if not tokens1 or not tokens2:
        return 0.0

    dictionary = corpora.Dictionary([tokens1, tokens2])

    bow_doc1 = dictionary.doc2bow(tokens1)
    bow_doc2 = dictionary.doc2bow(tokens2)
    corpus_bow = [bow_doc1, bow_doc2]

    tfidf_model = models.TfidfModel(corpus_bow, wglobal=smooth_idf)

    tfidf_doc1 = tfidf_model[bow_doc1]
    tfidf_doc2 = tfidf_model[bow_doc2]

    score = matutils.cossim(tfidf_doc1, tfidf_doc2)
    return float(score)