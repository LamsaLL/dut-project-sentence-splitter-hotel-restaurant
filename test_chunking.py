from chunking import acceptable_word, get_terms, get_tree
# Pour lancer les tests => python -m pytest test_chunking.py

def test_chunk():
    chunks= [chunk for chunk in get_terms(get_tree("merveilleux restaurant, super chambre, charmant petit hôtel, excellent séjour."))]
    assert [["merveilleux","restaurant"], ["super","chambre"], ["charmant", "petit", "hôtel"], ["excellent", "séjour"]] == chunks

def test_acceptable_word_len_is_1():
    assert acceptable_word("e") == False

def test_acceptable_word_len_is_2():
    assert acceptable_word("et") == True

def test_acceptable_word_len_is_27():
    assert acceptable_word("intergouvernementalisations") == True

def test_acceptable_word_len_is_28():
    assert acceptable_word("intergouvernementalisationss") == False

def test_acceptable_word_digit():
    assert acceptable_word("5") == True
