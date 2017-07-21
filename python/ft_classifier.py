import sys
import random
import fasttext
import process_functions as pf
import json
import codecs
import numpy

data = sys.argv[1]
training_data = sys.argv[2]
result_data = sys.argv[3]
true_false = sys.argv[4]
false_true = sys.argv[5]

data_f = open(data, 'r')   #dataset containing training and test datasets
train_f = open(training_data, 'w')  # save as trainging datasets
result_f = codecs.open(result_data, 'w', 'utf-8')  #save as test prediction result
true_false_f = open(true_false, 'w')
false_true_f= open(false_true, 'w')

test_text, test_label = pf.generate_train_and_test(data_f, train_f)

data_f.close()
train_f.close()

classifier = fasttext.supervised(training_data, "incall_experi1_model")
predict_labels = classifier.predict(test_text)
TP = 0
FN = 0
FP = 0
TN = 0
k = 0
j = 0
for i in range(len(predict_labels)):
        if test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                TP += 1
        elif test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                FN += 1
                k += 1
                true_false_f.write("%d. %s\n" %(k, test_text[i]) )
        elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                FP += 1
                j += 1
                false_true_f.write("%d. %s\n" %(j, test_text[i]) )
        elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                TN += 1

this_result = {
        "stats": {
                "TP": TP,
                "FN": FN,
                "FP": FP,
                "TN": TN,
                "precision": TP / float(TP + FP),
                "recall": TP / float(TP + FN)
                }
	}

json.dump(this_result, result_f)
result_f.write("\n")

true_false_f.close()
false_true_f.close()
result_f.close()

'''
#for word_ngrams in [1]:
num=0
for epoch in range(4, 21, 1):
	for dim in range(60, 220, 20):
		for lr in numpy.arange(0.01, 0.26, 0.01):
			num = num + 1
			print ("Tune parameter no.%d" %num)
			classifier = fasttext.supervised(training_data, "movement_model",
						lr=lr, dim=dim, epoch=epoch)
			predict_labels = classifier.predict(test_text)

			t_t = 0
                        t_f = 0
                        f_t = 0
                        f_f = 0
                        k = 0
			for i in range(len(predict_labels)):
				if test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                                        t_t += 1
                                elif test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                                        t_f += 1
                                        k += 1
                                        true_false_f.write("%d. %s\n" %(k, test_text[i]) )
                                elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                                        f_t += 1
                                elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                                        f_f += 1 

			this_result = {
				"prams": {
					"lr": lr,
					"dim": dim,
					"epoch": epoch,
                                        
				},
				"stats": {
					"t_t": t_t,
					"t_f": t_f,
					"f_t": f_t,
					"f_f": f_f,
					"precision": t_t / float(t_t + f_t),
					"recall": t_t / float(t_t + t_f)
				}
			}

			json.dump(this_result, result_f)
			result_f.write("\n")
true_false_f.close()
result_f.close()
'''


