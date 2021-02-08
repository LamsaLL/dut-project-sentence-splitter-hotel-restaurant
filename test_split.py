from split import split_sentences, split_text_into_words, check_relation, get_pos
# Pour lancer les tests => python -m pytest test_split.py

def test_number_of_segments():
	tests = [
	"Qualité des produits utilisés des plats bien dressés & délicieux une carte des vins très bien garnie temps d'attente raisonnable entre les plats très belle vue sur le gouffre d'Enfer service de qualité",
	"Un restaurant vraiment excellent. Un accueil au top. Service souriant et à l'écoute et les plats étaient vraiment délicieux. A refaire sans hésiter !",
	"Suite a son déménagement nous voulions essayer ce restaurant. très beau site avec des tables espacées. service agreable et discret. Repas très bon avec des mélanges réussis et bien dresses. a refaire",
	"Restaurant excellent. Personnel un peu hautain, mis à part sa le service est agréable, les jeunes serveurs sont très agréable.",
	"La nourriture EXCELLENTE, par contre beaucoup de mises en bouche pour faire patienter beaucoup d'attente le service laisse vraiment à désirer pas la hauteur ."
	]
	res = [5,5,5,4,2]

	for ind, review in enumerate(tests):
		assert len(split_sentences(review)) == res[ind]

def test_check_relation_chunk():
	sent = "Excellent accueil"
	keyword = "accueil"
	t_sent = split_text_into_words(sent)

	assert check_relation(sent, keyword, t_sent.index(keyword)) == 1

def test_check_relation_chunk_none():
	sent = "service impeccable, rapide et efficace"
	keyword = "service"
	t_sent = split_text_into_words(sent)

	assert check_relation(sent, keyword, t_sent.index(keyword)) == 0

def test_get_pos_0_8():
	sent = "pour commencer, le cuisine être bon mais accueil manquant de chaleur"
	t_sent = split_text_into_words(sent)
	keywords = ["cuisine", "accueil"]

	assert get_pos(t_sent, sent, keywords) == [0,8]
