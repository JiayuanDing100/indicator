from spacy.matcher import Matcher
from spacy.attrs import LOWER, DEP, FLAG29


def set_flag(nlp, token_l, flag):
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)


def load_agency_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    agency = ['agency', 'agncy', 'agenc', 'agencies']

    is_agency = FLAG29
    set_flag(nlp, agency, is_agency)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_agency: True}])

    matcher.add_entity(3)
    matcher.add_pattern(3, [{LOWER: "or"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "le"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "law"}, {LOWER: "enforcement"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "no"}, {is_agency: True}])
    matcher.add_pattern(3, [{DEP: "neg"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "ad"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "not"}, {LOWER: "a"}, {is_agency: True}])
    matcher.add_pattern(3, [{LOWER: "tire"}, {LOWER: "of"}, {is_agency: True}])

    return matcher


def post_process(matches, nlp_doc):
    agency = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id - 1] not in agency:
            agency[label_list[ent_id - 1]] = []
            agency[label_list[ent_id - 1]].append(nlp_doc[start:end])
        else:
            agency[label_list[ent_id - 1]].append(nlp_doc[start:end])
    return agency


def extract(nlp_doc, matcher):
    agency_matches = matcher(nlp_doc)
    agency = post_process(agency_matches, nlp_doc)

    return agency