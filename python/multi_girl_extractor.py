from spacy.matcher import Matcher
from spacy.attrs import LOWER, DEP, FLAG30, FLAG31, FLAG32, FLAG33, FLAG34, ORTH, LEMMA, TAG, IS_ALPHA

def set_flag(nlp, token_l, flag):
    # for t in token_l:
        # elst = map(''.join, itertools.product(*((c.upper(), c.LEMMA()) for c in t)))
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)

def load_multi_girl_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    multi_num = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'double', 'triple'] + [str(x) for x in range(2, 11)]

    girl = ['gal', 'girl', 'slut', 'cutie', 'hottie', 'lady', 'teen', 'teenager', 'chick', 'staff', 'gf', 'she']
    show = ['show', 'special', 'session', 'fantasy']
    dict_and = ['and', 'an', 'n', '&']

    is_multi_num = FLAG30
    is_girl = FLAG31
    is_show = FLAG33
    is_and = FLAG34
    set_flag(nlp, multi_num, is_multi_num)
    set_flag(nlp, girl, is_girl)
    set_flag(nlp, show, is_show)
    set_flag(nlp, dict_and, is_and)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_multi_num: True}, {is_girl: True, TAG:"NNS"}])
    matcher.add_pattern(1, [{is_multi_num: True}, {is_girl: True, TAG:"NNPS"}])
    matcher.add_pattern(1, [{LOWER: "duo"}])
    matcher.add_pattern(1, [{LOWER: "2"}, {ORTH: "-"}, {LOWER: "for"}, {ORTH: "-"}, {LOWER: "1"}])
    matcher.add_pattern(1, [{LEMMA: "double"}, {ORTH: "-"}, {LEMMA: "session"}])
    matcher.add_pattern(1, [{LEMMA: "three"}, {ORTH: "-"}, {LEMMA: "way"}]) 
    matcher.add_pattern(1, [{is_multi_num: True}, {LOWER: "for"}, {ORTH: "1"}])
    matcher.add_pattern(1, [{is_multi_num: True}, {LOWER: "for"}, {ORTH: "one"}])
    matcher.add_pattern(1, [{LEMMA: "double"}, {is_show: True}])
    matcher.add_pattern(1, [{is_multi_num: True}, {LOWER: "way"}])
    
    matcher.add_entity(4)
    matcher.add_pattern(4, [{LOWER: "a"}, {is_girl: True}])
    matcher.add_pattern(4, [{LOWER: "how"}, {is_girl: True}])
    matcher.add_pattern(4, [{LOWER: "for"}, {is_girl: True}])
    matcher.add_pattern(4, [{IS_ALPHA: True, DEP: "nmod"}, {is_girl: True}])
    matcher.add_pattern(4, [{is_girl: True}, {is_and: True}, {LEMMA: "gentleman"}])
    matcher.add_pattern(4, [{is_girl: True}, {ORTH: "&"}, {ORTH: "&"}, {LEMMA: "gentleman"}])
    matcher.add_pattern(4, [{is_girl: True}, {is_and: True}, {LEMMA: "guy"}])
    matcher.add_pattern(4, [{is_girl: True}, {ORTH: "&"}, {ORTH: "&"}, {LEMMA: "guy"}])
    matcher.add_pattern(4, [{LEMMA: "gentleman"}, {is_and: True}, {is_girl: True}])
    matcher.add_pattern(4, [{LEMMA: "gentleman"}, {ORTH: "&"}, {ORTH: "&"}, {is_girl: True}])
    matcher.add_pattern(4, [{LEMMA: "guy"}, {is_and: True}, {is_girl: True}])
    matcher.add_pattern(4, [{LEMMA: "guy"}, {ORTH: "&"}, {ORTH: "&"}, {is_girl: True}])
    matcher.add_pattern(4, [{LOWER: "she"}])

    return matcher

def post_process(matches, nlp_doc):
    multi_girl = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in multi_girl:
            multi_girl[label_list[ent_id-1]] = []
            multi_girl[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            multi_girl[label_list[ent_id-1]].append(nlp_doc[start:end])
    return multi_girl

def extract(nlp_doc, matcher):
    multi_girl_matches = matcher(nlp_doc)
    multi_girl = post_process(multi_girl_matches, nlp_doc)

    return multi_girl