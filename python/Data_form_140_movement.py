# coding: utf-8
import sys
import random



total_data_f = open("/home/ubuntu/dig_indicator/data/movement_data/movement_experiment/dataset_140_movement.txt", 'w')

test_lst = []
lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_neg.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_sn_p.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_pos.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break



lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_sp_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_p_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break

    
lst = []

neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_sp_sn.txt').read().splitlines()
for myline in neg_lines:
    test_lst.append(myline)
   

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/movement_data/movement_ne.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 22:
            break
        
random.shuffle(test_lst)
for i in test_lst:
    total_data_f.write("%s\n" % i)
    
total_data_f.close()

