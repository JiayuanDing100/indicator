# coding: utf-8
import random
import sys




data_pos = open("/home/ubuntu/dig_indicator/data/movement_data/movement_pos.txt", 'r')
data_sp_n = open("/home/ubuntu/dig_indicator/data/movement_data/movement_sp_n.txt", 'r')
data_sn_p = open("/home/ubuntu/dig_indicator/data/movement_data/movement_sn_p.txt", 'r')







'''
data_pos = open("/home/ubuntu/dig_indicator/data/incall_data/incall_pos.txt", 'r')
data_sp_n = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sp_n.txt", 'r')
data_sn_p = open("/home/ubuntu/dig_indicator/data/incall_data/incall_sn_p.txt", 'r')
data_ne = open("/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt", 'r')
'''

dataset = []
for line in data_pos:
    dataset.append('__label__TRUE'+' '+line)
for line in data_sp_n:
    dataset.append('__label__TRUE'+' '+line)

print "Negative:",len(dataset)

for line in data_sn_p:
    dataset.append('__label__FALSE'+' '+line)

data_pos.close()
data_sp_n.close()
data_sn_p.close()


total_data_f = open("/home/ubuntu/dig_indicator/data/movement_data/movement_experiment/dataset_experi2.txt", 'w')



data_neg_f = open('/home/ubuntu/dig_indicator/data/movement_data/movement_neg.txt', 'r')
data_neg_lst = []
k = 0
for line in data_neg_f:
    r = random.random()
    if r <= 0.01360633:
        data_neg_lst.append(('__label__FALSE'+' '+line).strip()+'\n')
        k += 1
        print k


data_ne_f = open('/home/ubuntu/dig_indicator/data/movement_data/movement_ne.txt', 'r')
data_ne_lst = []
j = 0
for line in data_ne_f:
    r = random.random()
    if r <= 0.00008730:
        data_ne_lst.append(('__label__FALSE'+' '+line).strip()+'\n')
        j += 1
        print j

for i in data_neg_lst:
    dataset.append(i)
for i in data_ne_lst:
    dataset.append(i)
print len(dataset) 

open('/home/ubuntu/dig_indicator/data/movement_data/movement_neg.txt').close()
open('/home/ubuntu/dig_indicator/data/movement_data/movement_ne.txt').close()

random.shuffle(dataset)

for i in dataset:
    total_data_f.write("%s" % i)


total_data_f.close()

