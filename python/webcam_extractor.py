from spacy.matcher import Matcher
from spacy.attrs import LOWER, DEP, FLAG29, FLAG30, ORTH, LEMMA, IS_ALPHA


def set_flag(nlp, token_l, flag):
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)


def load_webcam_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    cam = ['cam', 'skype', 'facetime', 'webcam', 'mfc', 'iml']
    provider = ['girls', 'girl', 'models', 'model', 'staffs', 'staff', 'latinas', 'latina', 'talent', 'supermodels', 'supermodel', 'princesses', 'princess']

    is_cam = FLAG29
    is_provider = FLAG30
    set_flag(nlp, cam, is_cam)
    set_flag(nlp, provider, is_provider)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_cam: True}])
    matcher.add_pattern(1, [{LOWER: "live"}, {LEMMA: "show"}])
    matcher.add_pattern(1, [{LEMMA: "video"}, {ORTH: "@"}])
    matcher.add_pattern(1, [{LOWER: "free", DEP: "amod"}, {LEMMA: "video"}])
    matcher.add_pattern(1, [{LOWER: "porno"}, {is_provider: True}])
    matcher.add_pattern(1, [{LEMMA: "add"}, {LOWER: "i"}])
    matcher.add_pattern(1, [{LOWER: "chaturbate"}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "i"}, {LOWER: "on"}, {LOWER: "http"}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "me"}, {LOWER: "on"}, {LOWER: "http"}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "i"}, {LOWER: "on"}, {LOWER: "https"}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "me"}, {LOWER: "on"}, {LOWER: "http"}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "i"}, {LOWER: "on"}, {LOWER: "www"}, {ORTH: "."}])
    matcher.add_pattern(1, [{LEMMA: "see"}, {LOWER: "me"}, {LOWER: "on"}, {LOWER: "www"}, {ORTH: "."}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LOWER: "i"}, {LOWER: "cam"}])
    matcher.add_pattern(4, [{LOWER: "cam"}, {LOWER: "to"}])
    matcher.add_pattern(4, [{LOWER: "you"}, {LOWER: "cam"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {is_cam: True}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "camshow"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "liveshow"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "skypeshow"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "livshow"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LOWER: "paypal"}, {LEMMA: "show"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "show"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "chaturbate"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "live"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "video"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "porno"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "girl"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "girl"}, {LEMMA: "webcam"}])
    matcher.add_pattern(4, [{is_cam: True, DEP: "nsubj"}, {IS_ALPHA: True}, {IS_ALPHA: True, DEP: "neg"}])
    matcher.add_pattern(4, [{LEMMA: "video", DEP: "nsubj"}, {IS_ALPHA: True}, {IS_ALPHA: True, DEP: "neg"}])
    matcher.add_pattern(4, [{is_cam: True, DEP: "conj"}, {IS_ALPHA: True}, {IS_ALPHA: True, DEP: "neg"}])
    matcher.add_pattern(4, [{LEMMA: "video", DEP: "conj"}, {IS_ALPHA: True}, {IS_ALPHA: True, DEP: "neg"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {is_cam: True}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "live"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "video"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "free"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "porno"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "chaturbate"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "camshow"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "liveshow"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LEMMA: "skypeshow"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "paypal"}, {LEMMA: "show"}])
    matcher.add_pattern(4, [{LOWER: "it"}, {LEMMA: "be"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{LOWER: "its"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{LOWER: "im"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{LOWER: "i"}, {LEMMA: "be"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{LOWER: "my"}, {LOWER: "name"}, {LEMMA: "be"}, {LEMMA: "cam"}])
    matcher.add_pattern(4, [{LEMMA: "cam"}, {LOWER: "here"}])

    return matcher


def post_process(matches, nlp_doc):
    webcam = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id - 1] not in webcam:
            webcam[label_list[ent_id - 1]] = []
            webcam[label_list[ent_id - 1]].append(nlp_doc[start:end])
        else:
            webcam[label_list[ent_id - 1]].append(nlp_doc[start:end])
    return webcam


def extract(nlp_doc, matcher):
    webcam_matches = matcher(nlp_doc)
    webcam = post_process(webcam_matches, nlp_doc)

    return webcam