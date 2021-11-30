# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:29:54 2021

@author: hp
NAMA: AGFAN HERRU PRATAMA HENDARSIN
NIM: 0640002100043
"""
print ("@@@@ @@@@ @@@@ @@@@ @@   @")
print ("@  @ @    @    @  @ @ @  @")
print ("@@@@ @ @@ @@@@ @@@@ @  @ @")
print ("@  @ @@@@ @    @  @ @   @@\n")

print('tuple 1: ')
a=('1021','1022', '1023', '1024', '1025', '1026', '1027', '1028', '1029', '1030', '1030')
b = ", ".join(a[0:3])
c = ", ".join(a[4:7])
d= ", ".join(a[8:11])
print((b,c,d))
print('rata rata dar tuple adalah: ')
print ([sum(map(float, filter(None, a[0:3])))/(len(a)-1),(sum(map(float, filter(None, a[4:7])))/(len(a)-1)),(sum(map(float, filter(None, a[8:11])))/(len(a)-1))])  
print('====== AGFAN HERRU PRATAMA HENDARSIN ======')
print('========= 064002100043 =========')
