import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from PIL import Image
import json
import csv
from csv import DictReader
from operator import itemgetter, attrgetter
import statistics


with open('kode_negara_lengkap.json', 'r') as f_in:
    data = json.load(f_in)
    for element in data['cantik']:
        if element['name'] == 'Albania':
            print(element['alpha-3'])
            break

#country = []
#a = open('kode_negara_lengkap.json', 'r')
#data = json.load(a)
#for element in data['cantik']:
    #country.append(element["name"])
#print(country)



    
with open('produksi_minyak_mentah.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(['ALB'])
print(rows)


ot = pd.read_csv('produksi_minyak_mentah.csv')

#Select specific columns of your dataframe

#select values based on criteria
aabb = ot[ot.tahun == 1978]
atahunn3 = list(aabb['kode_negara'].unique())
aproduksi3 = list(aabb['produksi'])
aacct = list(zip(atahunn3, aproduksi3))
aaset = sorted(aacct, key=itemgetter(1), reverse=True)
alst_1_newwt, alst_2_newwt = zip(*aaset)

asue = len(aproduksi3)
atahunbee = []
with open('kode_negara_lengkap.json', 'r') as kooo:
    data = json.load(kooo)
    for element in data['cantik']:
        for i in range(0, asue):
            if element['alpha-3'] == atahunn3[0+i]:
                atahunbee.append(element['name'])
                break
aacc = list(zip(atahunbee, aproduksi3))
aase = sorted(aacc, key=itemgetter(1), reverse=True)

alst_1_neww, alst_2_neww = zip(*aase)

aassuiook = []
for element in alst_2_neww:
    for i in range(0, asue):
        if element != 0.0:
            aassuiook.append(element)
            break
aadess = len(aassuiook)
aacc2 = list(zip(alst_1_neww[:aadess], aassuiook))
alst_1_neww2, alst_2_neww2 = zip(*aacc2)
asue2 = len(alst_1_neww2)
regioon = []
subregioon = []
kodenega = []
with open('kode_negara_lengkap.json', 'r') as kooo2:
    data = json.load(kooo2)
    for element in data['cantik']:
        for i in range(0, asue2):
            if element['name'] == alst_1_neww2[0+i]:
                regioon.append(element['region'])
                subregioon.append(element['sub-region'])
                kodenega.append(element['alpha-3'])
                break
aadess = len(aassuiook)
aacc2 = list(zip(alst_1_neww[:aadess], aassuiook))
alst_1_neww2, alst_2_neww2 = zip(*aacc2)
print(alst_1_neww2)
print(kodenega)
print(subregioon)
print(regioon)




