import sys
import process_functions as pf
import spacy
import outcall_extractor

input_file = sys.argv[1]
positive_text = sys.argv[2]
negative_text = sys.argv[3]

nlp = spacy.load('en')
outcall_matcher = outcall_extractor.load_outcall_matcher(nlp)
#incall_matcher = incall_extractor.load_outcall_matcher(nlp)
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
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        outcall = outcall_extractor.extract(nlp(t_simple_tokens), outcall_matcher)
        #incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        label = pf.process_extracted(outcall)
        if label == "NE":
            ne_f.write(sentence)
        elif label == "ONLY_P":
            positive_f.write(sentence)
        elif label == "ONLY_N":
            negative_f.write(sentence)
        elif label == "SP_SN":
            sp_sn_f.write(sentence)
        elif label == "SP_N":
            sp_n_f.write(sentence)
        elif label == "SN_P":
            sn_p_f.write(sentence)
        elif label == "ONLY_P_N":
            p_n_f.write(sentence)

positive_f.close()
negative_f.close()
sp_sn_f.close()
sp_n_f.close()
sn_p_f.close()
p_n_f.close()
ne_f.close()



'''
input_file = sys.argv[1]
sp_sn_f = open(sys.argv[2], 'w')
test_140 = open(sys.argv[3], 'w')
nlp = spacy.load('en')
outcall_matcher = outcall_extractor.load_outcall_matcher(nlp)
#incall_matcher = incall_extractor.load_incall_matcher(nlp)
nlp = pf.prep_nlp(nlp)

#for test_140
with open(input_file, 'r') as f:
    for index, sentence in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        outcall = outcall_extractor.extract(nlp(t_simple_tokens), outcall_matcher)
        #incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        label = pf.process_extracted(outcall)
        if label == "NE":
            test_140.write("__label__ne %s" % sentence)
        elif label == "ONLY_P":
            test_140.write("__label__pos %s" % sentence)
        elif label == "ONLY_N":
            test_140.write("__label__neg %s" % sentence)
        elif label == "SP_SN":
            test_140.write("__label__sp_sn %s" % sentence)
        elif label == "SP_N":
            test_140.write("__label__sp_n %s" % sentence)
        elif label == "SN_P":
            test_140.write("__label__sn_p %s" % sentence)
        elif label == "ONLY_P_N":
            test_140.write("__label__p_n %s" % sentence)
            
sp_sn_f.close()
test_140.close()

'''
