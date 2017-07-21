from spacy.matcher import Matcher
from spacy.attrs import LEMMA, IS_ASCII, DEP, FLAG23, FLAG24, FLAG25

def add_to_vocab(nlp, lst):
    for lexeme in lst:
        nlp.vocab[lexeme.lower().decode('utf8')]

def load_outcall_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    location = ['location', 'place', 'studio', 'apartment', 'home', 'house', 'hotel']

    add_to_vocab(nlp, location)

    location_ids = {nlp.vocab.strings[s.lower()] for s in location}
    hyphen_id = nlp.vocab.strings['-']
    ampersand_id = nlp.vocab.strings['&']

    is_hyphen = FLAG23
    is_ampersand = FLAG24
    is_location = FLAG25
    
    for lexeme in nlp.vocab:
        if lexeme.lower == hyphen_id:
            lexeme.set_flag(is_hyphen, True)
        if lexeme.lower == ampersand_id:
            lexeme.set_flag(is_ampersand, True)
        if lexeme.lower in location_ids:
            lexeme.set_flag(is_location, True)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{LEMMA: "outcall"}])
    matcher.add_pattern(1, [{LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "out"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "your"}, {is_location: True}])
    matcher.add_pattern(1, [{LEMMA: "out"}, {LEMMA: "and"}, {LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "out"}, {is_ampersand: True}, {LEMMA: "in"}, {LEMMA: "call"}])
    matcher.add_pattern(1, [{LEMMA: "visit"}, {LEMMA: "you"}])
    matcher.add_pattern(1, [{LEMMA: "mind"}, {LEMMA: "travel"}])
    matcher.add_pattern(1, [{LEMMA: "anywhere"}, {LEMMA: "and"}, {LEMMA: "everywhere"}])
    matcher.add_pattern(1, [{LEMMA: "prefer"}, {LEMMA: "residence"}])
    matcher.add_pattern(1, [{LEMMA: "prefer"}, {LEMMA: "hotel"}])
    matcher.add_pattern(1, [{LEMMA: "come"}, {LEMMA: "to"}, {LEMMA: "you"}])
    matcher.add_pattern(1, [{LEMMA: "will"}, {LEMMA: "travel"}])
    
    matcher.add_entity(2)
    matcher.add_pattern(2, [{LEMMA: "outcall"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{LEMMA: "out"}, {LEMMA: "call"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{LEMMA: "out"}, {is_hyphen: True}, {LEMMA: "call"}, {LEMMA: "only"}])
    matcher.add_pattern(2, [{LEMMA: "your", DEP: "amod"}, {is_location: True}])
    matcher.add_pattern(2, [{LEMMA: "your", DEP: "amod"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(2, [{LEMMA: "your", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(2, [{LEMMA: "your", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])

    matcher.add_entity(3)
    matcher.add_pattern(3, [{is_location: True}])
    matcher.add_pattern(3, [{LEMMA: "place"}])
    matcher.add_pattern(3, [{LEMMA: "be"}, {LEMMA: "place"}])
    matcher.add_pattern(3, [{LEMMA: "is"}, {LEMMA: "place"}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LEMMA: "house"}, {LEMMA: "wives"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {LEMMA: "have"}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {IS_ASCII: True}, {LEMMA: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {LEMMA: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "my", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(4, [{LEMMA: "my", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "outcall"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "out"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "outcall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LEMMA: "out"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "outcall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LEMMA: "out"}, {is_hyphen: True}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{LEMMA: "visit"}, {LEMMA: "your"}, {LEMMA: "city"}])
    matcher.add_pattern(4, [{IS_ASCII: True}, {LEMMA: "miss"}, {LEMMA: "out"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "out"}, {LEMMA: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "dep"}, {LEMMA: "no"}])
    
    return matcher

def post_process(matches, nlp_doc):
    outcall = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in outcall:
            outcall[label_list[ent_id-1]] = []
            outcall[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            outcall[label_list[ent_id-1]].append(nlp_doc[start:end])
    return outcall

def extract(nlp_doc, matcher):
    outcall_matches = matcher(nlp_doc)
    outcall = post_process(outcall_matches, nlp_doc)

    return outcall