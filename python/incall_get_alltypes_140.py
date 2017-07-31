import sys
import process_functions as pf
import spacy
import incall_extractor

# run this coding in EC2

input_file = sys.argv[1]   #original 140 datasets
sp_sn_f = open(sys.argv[2], 'w')
test_140 = open(sys.argv[3], 'w')
nlp = spacy.load('en')
incall_matcher = incall_extractor.load_incall_matcher(nlp)
#incall_matcher = incall_extractor.load_incall_matcher(nlp)
nlp = pf.prep_nlp(nlp)

#for test_140
with open(input_file, 'r') as f:
    for index, sentence in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        #incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        label = pf.process_extracted(incall)
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
