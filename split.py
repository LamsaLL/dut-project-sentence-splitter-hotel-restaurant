from sys import path

#path.append("F://SAVS//Projet Solike//DémonCanFly//solike-project//Answer//Tools")
from keywords import Keyword
from preprocessing import Preprocess
from spacy import load as load_spacy
from chunking import get_tree, get_terms
# from .chunking import get_tree, get_terms
from nltk import word_tokenize

nlp = load_spacy("fr_core_news_sm", disable=["ner", "tagger"])
keyword = Keyword()
preprocess = Preprocess()

def get_prep_sentences(review):
    """Return a list of preprocessed sentences"""

    sentences = split_text_into_sentences(review)

    return preprocess.preprocess(sentences)

def split_text_into_sentences(text) :
    """Split the text into individual sentences"""

    doc = nlp(text)

    return [sent.text for sent in doc.sents]

def split_text_into_words(sent):
    """Split the sentence into individual words"""

    return word_tokenize(sent)

def check_relation(sentence,keyword,index):
    """Return the index of the keyword in the noun chunk"""

    chunks = get_terms(get_tree(sentence))
    keyword_chunk = None

    for chunk in chunks:
        if keyword in chunk:
            keyword_chunk = chunk
            break

    if keyword_chunk is None:
        ind = 0
    else:
        ind = keyword_chunk.index(keyword)

    return ind

def get_pos(t_sent,sent, keywords):
    """Return a list of keywords positions in the sentence"""

    count = 0
    pos_list = []

    for ind,word in enumerate(t_sent):
        if word in keywords:
            count += 1
            if count == 1:
                pos_list.append(0) #si c'est le premier mot clé de la phrase alors on met la position à 0
            else:
                maj_pos = ind - check_relation(sent,word, ind)
                pos_list.append(maj_pos)

    return pos_list


def split_sentences(review):
    """Segment the review by important meaning (one keyword per segmented sentence)"""

    seg_sentences = []
    sentences = get_prep_sentences(review)

    for sent in sentences :
        keywords = keyword.get_keywords(sent)
        if len(keywords) >= 2:
            t_sent = split_text_into_words(sent)
            pos_list = get_pos(t_sent, sent,keywords)

            for ind, pos in enumerate(pos_list):
                if ind + 1 < len(pos_list):
                    tokens = t_sent[pos:pos_list[ind+1]]
                else:
                    tokens = t_sent[pos:]

                if not len(tokens) in range(1):
                    seg_sentences.append(" ".join(tokens))
        else :
            seg_sentences.append(sent)

    return seg_sentences


if __name__ == "__main__":

    review = "Qualité des plats utilisés, nourriture bien dressés & délicieux. Une carte des vins très bien garnie temps d'attente raisonnable entre les plats très belle vue sur le gouffre d'Enfer service de qualité"

    print(review)
    sentences_split = split_sentences(review)
    print(sentences_split)
