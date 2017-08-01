from spacy.matcher import Matcher
from spacy.attrs import IS_DIGIT, DEP, FLAG40, FLAG41, ORTH, IS_ALPHA, LEMMA

def set_flag(nlp, token_l, flag):
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)

def load_risky_activities_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    risky_activities = [
        'bareback',
        'uncovered',
        'bbbjtcim',
        'bbbj',
        'bbbjtc',
        'bbbjtcws',
        'bbbjwf',
        'bbfs',
        'anal',
        'greek',
        'rca',
        'swallow',
        'cim',
        'choke',
        'bdsm',
        'bondage',
        'gangbang',
        'hardcore'
    ]

    provider = [
        'girl',
        'girls',
        'model',
        'models',
        'staff',
        'staffs',
        'latina',
        'latinas',
        'talent',
        'talents',
        'supermodel',
        'supermodels',
        'princess',
        'princesses'
    ]


    is_risky_activities = FLAG40
    is_provider = FLAG41
    set_flag(nlp, risky_activities, is_risky_activities)
    set_flag(nlp, provider, is_provider)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_risky_activities: True}])

    matcher.add_entity(2)
    matcher.add_pattern(2, [{LEMMA: "hardcore"}, {LEMMA: "sex"}])
    matcher.add_pattern(2, [{LEMMA: "hardcore"}, {LEMMA: "service"}])
    
    matcher.add_entity(3)
    matcher.add_pattern(3, [{LEMMA: "hardcore"}])
    
    matcher.add_entity(4)
    matcher.add_pattern(4, [{LEMMA: "greek"}, {IS_DIGIT: True}])
    matcher.add_pattern(4, [{LEMMA: "greek"}, {is_provider: True}])
    matcher.add_pattern(4, [{LEMMA: "if", DEP: "mark"}, {IS_ALPHA: True, DEP: "ROOT"}, {is_risky_activities: True}])
    matcher.add_pattern(4, [{is_risky_activities: True}, {LEMMA: "sorry"}])

    return matcher

def post_process(matches, nlp_doc):
    risky_activities = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in risky_activities:
            risky_activities[label_list[ent_id-1]] = []
            risky_activities[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            risky_activities[label_list[ent_id-1]].append(nlp_doc[start:end])
    return risky_activities

def extract(nlp_doc, matcher):
    risky_activities_matches = matcher(nlp_doc)
    risky_activities = post_process(risky_activities_matches, nlp_doc)

    return risky_activities
