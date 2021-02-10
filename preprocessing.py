import nltk
import spacy
from nltk import word_tokenize
import unidecode
from string import punctuation

class Preprocess:
	"""Preprocessing class"""
	def __init__(self):
		"""Init method"""

		self.stoplist = set(punctuation) - set(",")
		self.nlp = spacy.load("fr_core_news_sm", disable=["ner", "parser"])

	def preprocess(self, sents):
		"""Remove punctuation and lemm datas"""
		res = []
		for sent in sents:
			comment = self.nlp(" ".join([unidecode.unidecode(word.lower()) for word in nltk.word_tokenize(sent)]))

			lemmatized = []

			for word in comment:
				lemma = word.lemma_.strip()

				if lemma not in self.stoplist:
					lemmatized.append(lemma)

			res.append(" ".join(lemmatized))

		return res


if __name__ == "__main__":
	preprocess = Preprocess()
	print(preprocess.preprocess(["j'aime la belle couleur de l'au bleue", ", yes je le pense vraiment !!!!!!"]))
