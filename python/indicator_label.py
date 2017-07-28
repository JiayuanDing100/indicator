import sys
import process_functions as pf
import spacy
import multi_girl_extractor
import credit_card_extractor
import incall_extractor
import movement_extractor
import risky_activities_extractor
import outcall_extractor
import agency_extractor

input_file = sys.argv[1]
positive_text = sys.argv[2]
negative_text = sys.argv[3]

nlp = spacy.load('en')
multi_girl_matcher = multi_girl_extractor.load_multi_girl_matcher(nlp)
nlp = pf.prep_nlp(nlp)

positive_f = open(positive_text, 'w')
negative_f = open(negative_text, 'w')
sp_sn_f = open(sys.argv[4], 'w')
sp_n_f = open(sys.argv[5], 'w')
sn_p_f = open(sys.argv[6], 'w')
p_n_f = open(sys.argv[7], 'w')
ne_f = open(sys.argv[8], 'w')

with open(input_file, 'r') as f:
    for index, sentence in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=True)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        multi_girl = multi_girl_extractor.extract(nlp(t_simple_tokens), multi_girl_matcher)
        label = pf.process_extracted(multi_girl)
        if label == "NE":
            ne_f.write(sentence.lower())
        elif label == "ONLY_P":
            positive_f.write(sentence.lower())
        elif label == "ONLY_N":
            negative_f.write(sentence.lower())
        elif label == "SP_SN":
            sp_sn_f.write(sentence.lower())
        elif label == "SP_N":
            sp_n_f.write(sentence.lower())
        elif label == "SN_P":
            sn_p_f.write(sentence.lower())
        elif label == "ONLY_P_N":
            p_n_f.write(sentence.lower())

positive_f.close()
negative_f.close()
sp_sn_f.close()
sp_n_f.close()
sn_p_f.close()
p_n_f.close()
ne_f.close()
