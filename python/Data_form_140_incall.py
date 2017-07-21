# coding: utf-8
import sys
import random



total_data_f = open("dataset_20.txt", 'w')

test_lst = []
lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_neg.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sn_p.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_pos.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break



lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sp_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break

lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_p_n.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break

    
lst = []
k = 0
for i in range(20000):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_sp_sn.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break


lst = []
k = 0
for i in range(200):
    neg_lines = open('/home/ubuntu/dig_indicator/data/incall_data/incall_ne.txt').read().splitlines()
    myline =random.choice(neg_lines)
    if myline not in lst:
        test_lst.append(myline)
        k += 1
        lst.append(myline)
        if k == 20:
            break
        
random.shuffle(test_lst)
for i in test_lst:
    total_data_f.write("%s\n" % i)
    
total_data_f.close()

