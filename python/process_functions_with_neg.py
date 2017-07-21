# coding: utf-8
import json
import string
import codecs
from tokenizer_extractor import TokenizerExtractor
import random

_LEAST_LEN = 10

def extract_crftokens(text, options=None, lowercase=False):
        t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        return t.extract(text, lowercase)

def extract_tokens_from_crf(crf_tokens):
        return [tk['value'] for tk in crf_tokens]

#given a string, split this string into many line according to new line symbol
def split_line(s):
    str_result = s.strip().translate(string.maketrans("", ""), string.punctuation)
    lst = [x.strip() for x in str_result.split('\n') if x != ' ']
    lst_result = []
    for i in lst:
        if len(i) >= _LEAST_LEN:
            lst_result.append(i)
    return lst_result


def prep_nlp(nlp):
    old_tokenizer = nlp.tokenizer
    nlp.tokenizer = lambda tokens: old_tokenizer.tokens_from_list(tokens)
    return nlp

def process_extracted(extracted_dict):
    if len(extracted_dict) == 0:
        return "FALSE"
    elif "strong positive" in extracted_dict and "strong negative" not in extracted_dict:
        return "TRUE"
    elif "strong positive" not in extracted_dict and "strong negative" in extracted_dict:
        return "FALSE"
    elif "strong positive" not in extracted_dict and "strong negative" not in extracted_dict:
        if "positive" in extracted_dict and "negative" not in extracted_dict:
            return "TRUE"
        elif "positive" not in extracted_dict and "negative" in extracted_dict:
            return "FALSE"
        else:
            return "FALSE"
    else:
        return "FALSE"

def generate_train_and_test(f, train_f):
    texts = []
    labels = []
    for line in f:
        r = random.random()
        if r <= 0.25:
            texts.append(line.strip().split(' ', 1)[1])
            labels.append(line.strip().split(' ', 1)[0].split('__')[-1])
        else:
            train_f.write("%s" % line)
    return [texts, labels]

