from spacy.matcher import Matcher
from spacy.attrs import LEMMA, IS_ASCII, IS_DIGIT, TAG, DEP, ENT_TYPE, FLAG23, FLAG24, FLAG25, FLAG26, FLAG27, LOWER

def add_to_vocab(nlp, lst):
    for lexeme in lst:
        nlp.vocab[lexeme.lower().decode('utf8')]

def load_incall_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    location = ['location', 'place', 'studio', 'apartment', 'home', 'house']
    private = ['private', 'discreet', 'discrete']
    clean = ['clean', 'nice', 'lovely']

    add_to_vocab(nlp, location)
    add_to_vocab(nlp, private)
    add_to_vocab(nlp, clean)

    location_ids = {nlp.vocab.strings[s.lower()] for s in location}
    private_ids = {nlp.vocab.strings[s.lower()] for s in private}
    clean_ids = {nlp.vocab.strings[s.lower()] for s in clean}
    hyphen_id = nlp.vocab.strings['-']
    ampersand_id = nlp.vocab.strings['&']
 
    is_hyphen = FLAG23
    is_ampersand = FLAG24
    is_location = FLAG25
    is_private = FLAG26
    is_clean = FLAG27

    for lexeme in nlp.vocab:
        if lexeme.lower == hyphen_id:
            lexeme.set_flag(is_hyphen, True)
        if lexeme.lower == ampersand_id:
            lexeme.set_flag(is_ampersand, True)
        if lexeme.lower in location_ids:
            lexeme.set_flag(is_location, True)
        if lexeme.lower in private_ids:
            lexeme.set_flag(is_private, True)
        if lexeme.lower in clean_ids:
            lexeme.set_flag(is_clean, True)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{LEMMA: "incall"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "and"}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {is_ampersand: True}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "visit"}, {LEMMA: "i"}])

    matcher.add_entity(2)
    matcher.add_pattern(2, [{LEMMA: "incall"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{LEMMA: "in"}, {LEMMA: "call"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{LEMMA: "in"}, {is_hyphen: True}, {LEMMA: "call"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{is_private: True, DEP: "amod"}, {is_location: True}])
    matcher.add_pattern(2, [{is_private: True, DEP: "amod"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(2, [{is_clean: True}, {is_location: True}])
    matcher.add_pattern(2, [{LEMMA: "my", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(2, [{LEMMA: "my", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])

    matcher.add_entity(3)
    matcher.add_pattern(3, [{LEMMA: "location"}])
    matcher.add_pattern(3, [{LEMMA: "place"}])
    matcher.add_pattern(3, [{LEMMA: "be"}, {LEMMA: "place"}])
    matcher.add_pattern(3, [{LEMMA: "is"}, {LEMMA: "place"}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LEMMA: "house"}, {LEMMA: "wife"}])
    matcher.add_pattern(4, [{LOWER: "your", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(4, [{LOWER: "your", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "incall"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "in"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "incall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "in"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "incall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "in"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "have"}, {IS_ASCII: True, DEP: "dobj"}])    
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {LEMMA: "have"}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {IS_ASCII: True}, {LEMMA: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {LEMMA: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])

    return matcher

def post_process(matches, nlp_doc):
    incall = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in incall:
            incall[label_list[ent_id-1]] = []
            incall[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            incall[label_list[ent_id-1]].append(nlp_doc[start:end])
    return incall

def extract(nlp_doc, matcher):
    incall_matches = matcher(nlp_doc)
    incall = post_process(incall_matches, nlp_doc)

    return incall