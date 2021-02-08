import nltk
from nltk import RegexpParser, word_tokenize
from nltk.tag import StanfordPOSTagger
import os

java_path = os.path.abspath(os.path.dirname(__file__)) + "/stanford-postagger/jre1.8.0_211"
os.environ['JAVAHOME'] = java_path

# 'ADV': 'adverb',
# 'ADJ : 'Adjective',
# 'CC': 'coordinating conjunction',
# 'Cl': 'weak clitic pronoun',
# 'CS': 'subordinating conjunction',
# 'D': 'determiner',
# 'ET': 'foreign word',
# 'I': 'interjection',
# 'NC': 'common noun',
# 'NP': 'proper noun',
# 'P': 'preposition',
# 'PP': 'group prepopositional',
# 'PREF': 'prefix',
# 'PRO': 'strong pronoun',
# 'V': 'verb',
# 'PONCT': 'punctuation mark',
# 'N': 'noun'
# 'DET' : determiner'

def get_tree(sentence):
    """Return a flatten nltk parse tree with chunks"""

    grammar = ('''
        ND: {<ADV>*<ADJ>?<IN>?<DET>?(<NC>+ |<NP>+ |<N>+)}
        VD: {<V.*>?<DET>?<ND>}
        Chunk: {<VD> | <ND>}
    ''')

    chunkParser = RegexpParser(grammar)
    # tagger = StanfordPOSTagger('stanford-postagger/models//french.tagger', path_to_jar= 'stanford-postagger/stanford-postagger.jar')
    tagger = StanfordPOSTagger(os.path.abspath(os.path.dirname(__file__)) +'/stanford-postagger/models//french.tagger', path_to_jar= os.path.abspath(os.path.dirname(__file__)) +'/stanford-postagger/stanford-postagger.jar')
    tagged = tagger.tag(word_tokenize(sentence))
    tree = chunkParser.parse(tagged)
	
    tree.draw()
	
    return tree

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""

    accepted = bool((2 <= len(word) <= 27) or word.isdigit())

    return accepted

def get_terms(tree):

    for leaf in get_leaves(tree):
        term = [ w for w,t in leaf if acceptable_word(w)]

        yield term

def get_leaves(tree):
    """Finds chunks leaf nodes of a chunk tree."""

    for subtree in tree.subtrees(filter = lambda t: t.label()=='Chunk'):

        yield subtree.leaves()


if __name__ == "__main__":
    review = "Restaurant excellent, les mets sont à la hauteur attendu au niveau de la renommée et bien évidemment du tarif. Personnel un peu hautain, mis à part sa le service est agréable, les jeunes serveurs sont très agréable."
    chunks = get_terms(get_tree(review))

    for chunk in chunks:
        print (chunk)
