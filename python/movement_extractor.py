from spacy.matcher import Matcher
from spacy.attrs import LEMMA, IS_ASCII, IS_DIGIT, FLAG18, FLAG19, FLAG20, TAG, DEP, ENT_TYPE, IS_ALPHA, LOWER

def add_to_vocab(nlp, lst):
    for lexeme in lst:
        nlp.vocab[lexeme.lower().decode('utf8')]

def load_movement_matcher(nlp):
    matcher = Matcher(nlp.vocab)
    
    place = ['area', 'place', 'city', 'town']
    girl = ['gal', 'girl', 'slut', 'cutie', 'hottie', 'lady', 'teen', 'teenager', 'chick', 'staff', 'gf', 'she']
    
    add_to_vocab(nlp, place)
    add_to_vocab(nlp, girl)
    
    is_place = FLAG18
    is_girl = FLAG19
    upper_start = FLAG20

    for lexeme in nlp.vocab:
        if lexeme.lower_ in place:
            lexeme.set_flag(is_place, True)
        if lexeme.lower_ in girl:
            lexeme.set_flag(is_girl, True)
        if lexeme.prefix_.isupper():
            lexeme.set_flag(upper_start, True)

    # Positive Matcher Patterns
    matcher.add_entity(1)
    matcher.add_pattern(1, [{LEMMA: "last"}, {LEMMA: "night"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {IS_ASCII: True, ENT_TYPE: "DATE"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {DEP: "partmod"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {DEP: "quantmod"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {IS_ASCII: True, ENT_TYPE: "TIME"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {LEMMA: "in"}, {IS_ASCII: True, ENT_TYPE: "DATE"}])
    matcher.add_pattern(1, [{LEMMA: "leave"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "out"}, {LEMMA: "of"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LOWER: "outta"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "lastnight"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "back"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "just"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "day"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "town"}, {LEMMA: "tonight"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "town"}, {LEMMA: "through"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "town"}, {LEMMA: "until"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "town"}, {LEMMA: "for"}, {LEMMA: "one"}, {LEMMA: "night"}])
    matcher.add_pattern(1, [{LEMMA: "in"}, {LEMMA: "town"}, {LEMMA: "for"}, {IS_DIGIT: True}, {LEMMA: "night"}])
    matcher.add_pattern(1, [{LEMMA: "town"}, {LEMMA: "stay", DEP: "nmod"}])
    matcher.add_pattern(1, [{LEMMA: "town"}, {IS_ASCII: True}, {LEMMA: "stay", DEP: "nmod"}])
    matcher.add_pattern(1, [{LEMMA: "new"}, {LEMMA: "girl"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(1, [{LEMMA: "recent"}, {LEMMA: "move"}])
    matcher.add_pattern(1, [{LEMMA: "recently"}, {LEMMA: "move"}])
    matcher.add_pattern(1, [{LEMMA: "relocate"}])
    matcher.add_pattern(1, [{LEMMA: "new", DEP: "amod"}, {LEMMA: "city"}, {LEMMA: "to", DEP: "dep"}])
    matcher.add_pattern(1, [{LEMMA: "new", DEP: "amod"}, {IS_ASCII: True}, {LEMMA: "city"}, {IS_ASCII: True}, {LEMMA: "to", DEP: "dep"}])
    matcher.add_pattern(1, [{LEMMA: "new"}, {LEMMA: "to"}, {LEMMA: "area"}])
    matcher.add_pattern(1, [{LEMMA: "new"}, {LEMMA: "to"}, {upper_start: True}])
    matcher.add_pattern(1, [{LEMMA: "first"}, {LEMMA: "visit"}, {LEMMA: "to"}])
    matcher.add_pattern(1, [{LEMMA: "i", DEP: "nsubj"}, {LEMMA: "arrive"}])
    matcher.add_pattern(1, [{LEMMA: "girl", DEP: "nsubj"}, {LEMMA: "arrive"}, {DEP: "partmod"}])
    matcher.add_pattern(1, [{LEMMA: "girl", DEP: "nsubj"}, {IS_ASCII: True}, {LEMMA: "arrive"}, {IS_ASCII: True}, {DEP: "partmod"}])
    matcher.add_pattern(1, [{LEMMA: "girl", DEP: "nsubj"}, {LEMMA: "arrive"}, {DEP: "quantmod"}])
    matcher.add_pattern(1, [{LEMMA: "girl", DEP: "nsubj"}, {IS_ASCII: True}, {LEMMA: "arrive"}, {IS_ASCII: True}, {DEP: "quantmod"}])
    matcher.add_pattern(1, [{LEMMA: "just"}, {LEMMA: "arrive"}])
    matcher.add_pattern(1, [{LEMMA: "on"}, {LEMMA: "my"}, {LEMMA: "way"},{LEMMA: "to"},{TAG: "NNP"}])
    matcher.add_pattern(1, [{LEMMA: "on"}, {LEMMA: "my"}, {LEMMA: "way"},{LEMMA: "to"},{TAG: "NN"}])
    matcher.add_pattern(1, [{LEMMA: "on"}, {LEMMA: "the"}, {LEMMA: "way"}])
    matcher.add_pattern(1, [{LEMMA: "just"}, {LEMMA: "get"}, {LEMMA: "here"}])
    matcher.add_pattern(1, [{LEMMA: "get"}, {LEMMA: "here"}, {LEMMA: "today"}])
    matcher.add_pattern(1, [{LEMMA: "get"}, {LEMMA: "here"}, {LEMMA: "yesterday"}])
    matcher.add_pattern(1, [{LEMMA: "get"}, {LEMMA: "here"}, {LEMMA: "last"}, {LEMMA: "night"}])
    matcher.add_pattern(1, [{LEMMA: "i", DEP: "nsubj"}, {IS_ASCII: True}, {LEMMA: "visit"}, {IS_ASCII: True}, {is_place: True, DEP: "dobj"}])
    matcher.add_pattern(1, [{LEMMA: "i", DEP: "nsubj"}, {LEMMA: "visit"}, {is_place: True, DEP: "dobj"}])

    # Strong Positive Matcher Patterns
    matcher.add_entity(2)
    matcher.add_pattern(2, [{LEMMA: "new"}, {IS_ASCII: True}, {LEMMA: "in"}, {is_place: True}])
    matcher.add_pattern(2, [{LEMMA: "new"}, {IS_ASCII: True}, {IS_ASCII: True}, {LEMMA: "in"}, {is_place: True}])
    matcher.add_pattern(2, [{LEMMA: "im"}, {LEMMA: "new"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(2, [{LEMMA: "new"}, {LEMMA: "in"}, {is_place: True}])
    matcher.add_pattern(2, [{LEMMA: "new"}, {LEMMA: "to"}, {is_place: True}])
    matcher.add_pattern(2, [{LEMMA: "new"}, {is_girl: True}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(2, [{LEMMA: "new"}, {LEMMA: "to"}, {upper_start: True}, {LEMMA: "area"}])


    # Negative Matcher Patterns
    matcher.add_entity(3)
    matcher.add_pattern(3, [{LEMMA: "new"}])
    matcher.add_pattern(3, [{LEMMA: "girl"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(3, [{LEMMA: "grand"}, {LEMMA: "new"}])
    matcher.add_pattern(3, [{LEMMA: "new"}, {LEMMA: "at"}])
    matcher.add_pattern(3, [{LEMMA: "new"}, {LEMMA: "to"}, {LEMMA: "business"}])
    matcher.add_pattern(3, [{LEMMA: "new"}, {LEMMA: "to"}, {LEMMA: "industry"}])
    matcher.add_pattern(3, [{LEMMA: "new"}, {LEMMA: "to"}, {LEMMA: "scenario"}])
    matcher.add_pattern(3, [{LEMMA: "dream", DEP: "nsubj"}, {LEMMA: "arrive"}])
    matcher.add_pattern(3, [{LEMMA: "fantasy", DEP: "nsubj"}, {LEMMA: "arrive"}])
    matcher.add_pattern(3, [{LEMMA: "you", DEP: "nsubj"},  {LEMMA: "arrive"}])
    matcher.add_pattern(3, [{LEMMA: "area"}, {LEMMA: "only"}])
    matcher.add_pattern(3, [{upper_start: True}, {LEMMA: "area"}])
    matcher.add_pattern(3, [{LEMMA: "you", DEP: "nsubj"}, {LEMMA: "leave"}])
    matcher.add_pattern(3, [{LEMMA: "it", DEP: "dobj"}, {LEMMA: "leave"}, {IS_ASCII: True, DEP: "nmod", TAG: "TO"}])
    matcher.add_pattern(3, [{LEMMA: "that", DEP: "dobj"}, {LEMMA: "leave"}, {IS_ASCII: True, DEP: "nmod", TAG: "TO"}])
    matcher.add_pattern(3, [{LEMMA: "best"}, {LEMMA: "move"}])
    matcher.add_pattern(3, [{LEMMA: "next"}, {LEMMA: "move"}])
    matcher.add_pattern(3, [{LEMMA: "arrive"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "xcomp"}])
    matcher.add_pattern(3, [{LEMMA: "arrive"}, {IS_ASCII: True, DEP: "xcomp"}])
    matcher.add_pattern(3, [{LEMMA: "visit"}, {LEMMA: "sister", DEP: "dobj"}])
    matcher.add_pattern(3, [{LEMMA: "visit"}, {IS_ASCII: True}, {LEMMA: "sister", DEP: "dobj"}])
    matcher.add_pattern(3, [{LEMMA: "visit"}, {LEMMA: "family", DEP: "dobj"}])
    matcher.add_pattern(3, [{LEMMA: "visit"}, {IS_ASCII: True}, {LEMMA: "family", DEP: "dobj"}])
    matcher.add_pattern(3, [{LEMMA: "we", DEP: "poss"}, {LEMMA: "visit"}])

    # Strong Negative Matcher Patterns
    matcher.add_entity(4)
    matcher.add_pattern(4, [{LEMMA: "town"}, {LEMMA: "girl"}])
    matcher.add_pattern(4, [{LEMMA: "on"}, {LEMMA: "the"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "near"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "down"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "town"}, {LEMMA: "hall"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {IS_ASCII: True}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {IS_ASCII: True}, {IS_ASCII: True}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {LEMMA: "in"}, {IS_ASCII: True}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {IS_ASCII: True}, {LEMMA: "in"}, {IS_ASCII: True}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "best"}, {IS_ASCII: True}, {IS_ASCII: True}, {LEMMA: "in"}, {IS_ASCII: True}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "not"}, {LEMMA: "new"}, {LEMMA: "in"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "not"}, {LEMMA: "new"}, {LEMMA: "to"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "not"}, {LEMMA: "leave"}, {LEMMA: "town"}])	
    matcher.add_pattern(4, [{LEMMA: "i", DEP: "nsubj"}, {LEMMA: "leave"}, {LEMMA: "you", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {LEMMA: "but"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {LEMMA: "backpage", DEP: "nmod", TAG: "TO"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {IS_ASCII: True}, {LEMMA: "backpage", DEP: "nmod", TAG: "TO"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {LEMMA: "bp", DEP: "nmod", TAG: "TO"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {IS_ASCII: True}, {LEMMA: "bp", DEP: "nmod", TAG: "TO"}])
    #DS
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "message", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "msg", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "txt", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "text", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "impression", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "voicemail", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "smile", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "message", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "msg", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "txt", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "text", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "impression", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "voicemail", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "smile", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "satisfied"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "memory", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {IS_ASCII: True}, {LEMMA: "memory", DEP: "dobj"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "you"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "u"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "with"}])
    matcher.add_pattern(4, [{LEMMA: "leave"}, {LEMMA: "a"}, {LEMMA: "gentleman"}])
    matcher.add_pattern(4, [{LEMMA: "or"}, {LEMMA: "leave"}])
    matcher.add_pattern(4, [{LEMMA: "or"}, {LEMMA: "i"}, {LEMMA: "leave"}])
    matcher.add_pattern(4, [{LEMMA: "move"}, {LEMMA: "on"}])
    matcher.add_pattern(4, [{LEMMA: "i"}, {LEMMA: "move"}, {LEMMA: "like"}])
    matcher.add_pattern(4, [{LEMMA: "arrive"}, {LEMMA: "on"}, {LEMMA: "time"}])
    matcher.add_pattern(4, [{LEMMA: "can"}, {LEMMA: "move"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {LEMMA: "but"}])
    matcher.add_pattern(4, [{LEMMA: "on"}, {LEMMA: "my"}, {LEMMA: "way"}, {LEMMA: "to"}, {TAG: "PRP"}])
    matcher.add_pattern(4, [{LEMMA: "u"}, {LEMMA: "get"}, {LEMMA: "here"}])
    matcher.add_pattern(4, [{LEMMA: "you"}, {LEMMA: "get"}, {LEMMA: "here"}])
    matcher.add_pattern(4, [{LEMMA: "go"}, {LEMMA: "to"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LEMMA: "new"}, {LEMMA: "management"}])

    return matcher

def post_process(matches, nlp_doc):
    movement = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in movement:
            movement[label_list[ent_id-1]] = []
            movement[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            movement[label_list[ent_id-1]].append(nlp_doc[start:end])
    return movement

def extract(nlp_doc, matcher):
    movement_matches = matcher(nlp_doc)
    movement = post_process(movement_matches, nlp_doc)

    return movement