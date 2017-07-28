from spacy.matcher import Matcher
from spacy.attrs import LOWER, DEP, FLAG29, FLAG30, LEMMA, IS_ALPHA, POS


def set_flag(nlp, token_l, flag):
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)


def load_derogatory_mentions_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    bitch = ['whore', 'bitch', 'cunt', 'psycho', 'slut']
    your = ['your', 'ur']

    is_bitch = FLAG29
    is_your = FLAG30
    set_flag(nlp, bitch, is_bitch)
    set_flag(nlp, your, is_your)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_bitch: True}])
    matcher.add_pattern(1, [{LEMMA: "expose"}, {LOWER: "i"}])
    matcher.add_pattern(1, [{LEMMA: "expose"}, {LOWER: "me"}])
    matcher.add_pattern(1, [{LEMMA: "violate"}, {LOWER: "i"}])
    matcher.add_pattern(1, [{LEMMA: "violate"}, {LOWER: "me"}])
    matcher.add_pattern(1, [{LEMMA: "fuck"}, {LOWER: "i"}])
    matcher.add_pattern(1, [{LEMMA: "fuck"}, {LOWER: "me"}])
    matcher.add_pattern(1, [{LOWER: "i", DEP: "nsubj"}, {IS_ALPHA: True}, {LEMMA: "violate", DEP: "xcomp"}])
    matcher.add_pattern(1, [{LEMMA: "piece"}, {LOWER: "of"}, {LEMMA: "shit"}])
    matcher.add_pattern(1, [{LOWER: "hardcore"}])
    matcher.add_pattern(1, [{is_your: True}, {is_bitch: True}])
    matcher.add_pattern(1, [{is_your: True}, {LEMMA: "slave"}])
    matcher.add_pattern(1, [{is_your: True, DEP: "poss"}, {is_bitch: True}])
    matcher.add_pattern(1, [{is_your: True}, {LEMMA: "slave"}])
    matcher.add_pattern(1, [{LOWER: "i", DEP: "nsubj"}, {is_bitch: True}])
    matcher.add_pattern(1, [{LOWER: "i", DEP: "nsubj"}, {IS_ALPHA: True}, {is_bitch: True, DEP: "xcomp"}])

    matcher.add_entity(3)
    matcher.add_pattern(3, [{LOWER: "like"}, {is_bitch: True}])
    matcher.add_pattern(3, [{LEMMA: "bitch", POS: "VERB"}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LOWER: "to"}, {is_bitch: True}])
    matcher.add_pattern(4, [{LOWER: "nor"}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "slave"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "expose"}, {LOWER: "i"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "expose"}, {LOWER: "me"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "piece"}, {LOWER: "of"}, {LEMMA: "shit"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {is_your: True}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "slave"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "expose"}, {LOWER: "i"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "expose"}, {LOWER: "me"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "piece"}, {LOWER: "of"}, {LEMMA: "shit"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {is_your: True}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "slave"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "expose"}, {LOWER: "i"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "expose"}, {LOWER: "me"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {LEMMA: "piece"}, {LOWER: "of"}, {LEMMA: "shit"}])
    matcher.add_pattern(4, [{LEMMA: "girl"}, {LOWER: "next"}, {LEMMA: "door"}])
    matcher.add_pattern(4, [{LOWER: "with"}, {LOWER: "my"}, {LEMMA: "girl"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {is_bitch: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LOWER: "like"}, {is_bitch: True}])
    matcher.add_pattern(4, [{LEMMA: "look"}, {LEMMA: "slave", DEP: "prep"}])
    matcher.add_pattern(4, [{LOWER: "you"}, {is_bitch: True}])
    matcher.add_pattern(4, [{LOWER: "you"}, {POS: "ADJ"}, {is_bitch: True}])

    return matcher


def post_process(matches, nlp_doc):
    derogatory_mentions = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id - 1] not in derogatory_mentions:
            derogatory_mentions[label_list[ent_id - 1]] = []
            derogatory_mentions[label_list[ent_id - 1]].append(nlp_doc[start:end])
        else:
            derogatory_mentions[label_list[ent_id - 1]].append(nlp_doc[start:end])
    return derogatory_mentions


def extract(nlp_doc, matcher):
    derogatory_mentions_matches = matcher(nlp_doc)
    derogatory_mentions = post_process(derogatory_mentions_matches, nlp_doc)

    return derogatory_mentions
