from spacy.matcher import Matcher
from spacy.attrs import LOWER, IS_ASCII, DEP, FLAG40, FLAG41, ORTH, LEMMA

def set_flag(nlp, token_l, flag):
    # for t in token_l:
        # elst = map(''.join, itertools.product(*((c.upper(), c.LEMMA()) for c in t)))
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)

def load_credit_card_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    payment =  [
        'visa',
        'mastercard',
        'masterc',
        'mc',
        'mcard',
        'cash',
        'csh',
        'discover',
        'amex',
        'interac',
        'jcb'
    ]

    visa_type =  [
        'us',
        'american',
        'canadian',
        'student',
        'online',
        'transit',
        'need',
        'make',
        'f1',
        'temp',
        'temporary',
        'permanent',
        'visitor',
        'visit',
        'visiting'
    ]

    is_payment = FLAG40
    is_visa_type = FLAG41
    set_flag(nlp, payment, is_payment)
    set_flag(nlp, visa_type, is_visa_type)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "/"}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: ","}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {LEMMA: "and"}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "/"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: ","}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "&"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {LEMMA: "and"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {ORTH: "/"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {ORTH: ","}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {LEMMA: "and"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {ORTH: "/"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {ORTH: ","}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {ORTH: "&"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}, {LEMMA: "and"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LEMMA: "diners"}, {LEMMA: "club"}, {LEMMA: "internacional"}])
    matcher.add_pattern(1, [{LOWER: "union"}, {LOWER: "pay"}])
    matcher.add_pattern(1, [{LEMMA: "credit"}, {LEMMA: "card"}])
    matcher.add_pattern(1, [{LEMMA: "creditcard"}])

    matcher.add_entity(2)
    matcher.add_pattern(2, [{LEMMA: "accept"}, {LEMMA: "card"}])
    matcher.add_pattern(2, [{LEMMA: "accept"}, {is_payment: True}])
    matcher.add_pattern(2, [{LEMMA: "accept"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(2, [{LEMMA: "accept"}, {ORTH: ":"}, {is_payment: True}])
    matcher.add_pattern(2, [{LEMMA: "payment"}, {ORTH: ":"}, {is_payment: True}])
    matcher.add_pattern(2, [{LEMMA: "accept"}, {ORTH: ":"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(2, [{LEMMA: "payment"}, {ORTH: ":"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])    

    matcher.add_entity(3)
    matcher.add_pattern(3, [{LEMMA: "at"}, {is_payment: True}])
    matcher.add_pattern(3, [{LEMMA: "at"}, {LEMMA: "m"}, {ORTH: "/"}, {LEMMA: "card"}])
    matcher.add_pattern(3, [{LEMMA: "visa"}, {LEMMA: "versa"}])  
    
    matcher.add_entity(4)
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "credit"}, {LEMMA: "card"}])
    matcher.add_pattern(4, [{LEMMA: "credit"}, {LEMMA: "card"}, {DEP: "neg"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LEMMA: "creditcard"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "credit"}, {LEMMA: "card"}])
    matcher.add_pattern(4, [{LEMMA: "no"}, {LEMMA: "creditcard"}])
    matcher.add_pattern(4, [{LEMMA: "not"}, {IS_ASCII: True}, {LEMMA: "credit"}, {LEMMA: "card"}])
    matcher.add_pattern(4, [{LEMMA: "not"}, {IS_ASCII: True}, {LEMMA: "creditcard"}])
    matcher.add_pattern(4, [{is_visa_type: True}, {LEMMA: "visa"}])
    matcher.add_pattern(4, [{LEMMA: "visa"}, {LEMMA: "student"}])
    matcher.add_pattern(4, [{LEMMA: "rent"}, {LEMMA: "and"}, {LEMMA: "visa"}])
    matcher.add_pattern(4, [{LEMMA: "rent"}, {LEMMA: "and"}, {LEMMA: "credit"}])
    matcher.add_pattern(4, [{LEMMA: "visa"}, {LEMMA: "and"}, {LEMMA: "rent"}])
    matcher.add_pattern(4, [{LEMMA: "card"}, {LEMMA: "and"}, {LEMMA: "rent"}])
    matcher.add_pattern(4, [{LEMMA: "apply", DEP: "ROOT"}, {LEMMA: "for", DEP: "prep"}, {LEMMA: "visa"}])
    matcher.add_pattern(4, [{LEMMA: "apply", DEP: "ROOT"}, {LEMMA: "visa"}])
    matcher.add_pattern(4, [{LEMMA: "arrival", DEP: "ROOT"}, {LEMMA: "visa"}])

    return matcher

def post_process(matches, nlp_doc):
    credit_card = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in credit_card:
            credit_card[label_list[ent_id-1]] = []
            credit_card[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            credit_card[label_list[ent_id-1]].append(nlp_doc[start:end])
    return credit_card

def extract(nlp_doc, matcher):
    credit_card_matches = matcher(nlp_doc)
    credit_card = post_process(credit_card_matches, nlp_doc)

    return credit_card