from spacy.matcher import Matcher
from spacy.attrs import LOWER, DEP, FLAG29, FLAG30, LEMMA, IS_ALPHA, POS, IS_DIGIT


def set_flag(nlp, token_l, flag):
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)


def load_hotel_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    hotel = ['hotel', 'motel', 'inn', 'hotels', 'motels', 'inns']
    dict_and = ['and', 'n', 'an', 'nd', '&', '/']

    is_hotel = FLAG29
    is_and = FLAG30
    set_flag(nlp, hotel, is_hotel)
    set_flag(nlp, dict_and, is_and)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_hotel: True}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LEMMA: "inn"}, {is_and: True}, {LOWER: "out"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {is_and: True}, {LOWER: "outcall"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {LOWER: "call"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {is_and: True}, {LOWER: "outcalls"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {LOWER: "calls"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {IS_DIGIT: True}])
    matcher.add_pattern(4, [{LEMMA: "come"}, {LEMMA: "inn"}])
    matcher.add_pattern(4, [{LEMMA: "inn"}, {LEMMA: "town"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {is_hotel: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {is_hotel: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {IS_ALPHA: True}, {is_hotel: True}])

    return matcher


def post_process(matches, nlp_doc):
    hotel = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id - 1] not in hotel:
            hotel[label_list[ent_id - 1]] = []
            hotel[label_list[ent_id - 1]].append(nlp_doc[start:end])
        else:
            hotel[label_list[ent_id - 1]].append(nlp_doc[start:end])
    return hotel


def extract(nlp_doc, matcher):
    hotel_matches = matcher(nlp_doc)
    hotel = post_process(hotel_matches, nlp_doc)

    return hotel
