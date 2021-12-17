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

st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called

image = Image.open('3.png')
st.image(image)
############### title ###############)

############### sidebarr ###############


st.sidebar.title("Fadya Zalfa Rahmanita\n12220152")


## User inputs on the control panel #########
st.sidebar.subheader("Pengaturan Konfigurasi Grafik")
singkatan_country = []
country = []
a = open('kode_negara_lengkap.json', 'r')
data = json.load(a)
for element in data['cantik']:
    country.append(element["name"])
######### Grafik 1 #########
st.sidebar.caption('Pengaturan Grafik 1')
list_country = st.sidebar.selectbox("Pilih Negara", country)
with open('kode_negara_lengkap.json', 'r') as ko:
    data = json.load(ko)
    for element in data['cantik']:
        if element['name'] == list_country:
            sing = element['alpha-3']
            break
######### Grafik 2 #########
st.sidebar.caption('Pengaturan Grafik 2')
tah = st.sidebar.number_input("Jumlah negara", min_value=1, max_value=None, value=3)
tah2 = st.sidebar.number_input("Pada tahun: *1971-2015", min_value=1, max_value=None, value=1971)
############### For Grafik 1 ###############
st.subheader("Grafik 1")
ot = pd.read_csv('produksi_minyak_mentah.csv')
ab = ot[ot.kode_negara == sing]
st.dataframe(ab)
tahunn = list(ab['tahun'].unique())
produksi = list(ab['produksi'])

cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(tahunn)]
fig, ax = plt.subplots()
ax.bar(tahunn, produksi, color=colors)
ax.set_xlabel("Tahun", fontsize=12)
ax.set_ylabel("Jumlah Produksi", fontsize=12)
st.pyplot(fig)

############### For Grafik 2 ###############
st.subheader("Grafik 2")
ap = ot[ot.tahun == tah2]
st.dataframe(ap)
tahunn2 = list(ap['kode_negara'].unique())
produksi2 = list(ap['produksi'])
sue = len(tahunn2)
tahunbe = []
with open('kode_negara_lengkap.json', 'r') as koo:
    data = json.load(koo)
    for element in data['cantik']:
        for i in range(0, sue):
            if element['alpha-3'] == tahunn2[0+i]:
                tahunbe.append(element['name'])
                break
ac = list(map(list, zip(tahunbe, produksi2)))
ase = sorted(ac, key=itemgetter(1), reverse=True)
ajee = ase[:tah]
lst_1_new, lst_2_new = zip(*ajee)

cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(ajee)]
fig, ax = plt.subplots()
ax.bar(lst_1_new, lst_2_new, color=colors)
ax.set_xlabel("Negara", fontsize=12)
ax.set_ylabel("Jumlah Produksi", fontsize=12)
st.pyplot(fig)
############### For Grafik 3 ###############
st.sidebar.caption('Pengaturan Grafik 3')
tah3 = st.sidebar.number_input("Pada tahun: *1971-2015", min_value=1, max_value=None, value=1978)
st.subheader("Grafik 3")
abb = ot[ot.tahun == tah3]
st.dataframe(abb)
tahunn3 = list(abb['kode_negara'].unique())
produksi3 = list(abb['produksi'])
tahunbee = []
with open('kode_negara_lengkap.json', 'r') as koo:
    data = json.load(koo)
    for element in data['cantik']:
        for i in range(0, sue):
            if element['alpha-3'] == tahunn3[0+i]:
                tahunbee.append(element['name'])
                break
acc = list(zip(tahunbee, produksi3))
asee = sorted(acc, key=itemgetter(1), reverse=True)
lst_1_neww, lst_2_neww = zip(*asee)
suee = len(lst_2_neww)
assuiook = []
for element in lst_2_neww:
    for i in range(0, suee):
        if element != 0.0:
            assuiook.append(element)
            break
accuu = len(assuiook)
ajeee2 = lst_1_neww[:accuu]

cmap_name = 'tab20'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(assuiook)]
fig, ax = plt.subplots()
ax.bar(ajeee2, assuiook, color=colors)
ax.set_xlabel("Negara", fontsize=12)
ax.set_ylabel("Jumlah Produksi", fontsize=12)
st.pyplot(fig)
############### For 4 ###############
st.sidebar.caption('Pengaturan Jumlah Produksi Data')
tahh4 = st.sidebar.number_input("Pada tahun: *1971-2015", min_value=1, max_value=None, value=1979)
aabb = ot[ot.tahun == tahh4]
atahunn3 = list(aabb['kode_negara'].unique())
aproduksi3 = list(aabb['produksi'])
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
asue2 = len(alst_1_neww)
regioon = []
subregioon = []
kodenega = []
with open('kode_negara_lengkap.json', 'r') as kooo2:
    data = json.load(kooo2)
    for element in data['cantik']:
        for i in range(0, asue2):
            if element['name'] == alst_1_neww[0+i]:
                regioon.append(element['region'])
                subregioon.append(element['sub-region'])
                kodenega.append(element['alpha-3'])
                break
aassuiook = []
for element in alst_2_neww:
    for i in range(0, asue):
        if element != 0.0:
            aassuiook.append(element)
            break
aadess = len(aassuiook)
aacc2 = list(zip(alst_1_neww[:aadess], aassuiook))
alst_1_neww2, alst_2_neww2 = zip(*aacc2)

left_col, right_col = st.columns(2)
left_col.subheader("Negara Dengan Produksi Minyak Tertinggi")
left_col.text(f"Nama Negara: {alst_1_neww[0]}")
left_col.text(f"Kode Negara: {kodenega[0]}")
left_col.text(f"Region: {regioon[0]}")
left_col.text(f"Sub Region: {subregioon[0]}")
left_col.text(f"Produksi Terbesar: {alst_2_neww[0]}")
ot = pd.read_csv('produksi_minyak_mentah.csv')
absau = ot[ot.kode_negara == kodenega[0]]
left_col.dataframe(absau)
aloio = aadess - 1
right_col.subheader("Negara Dengan Produksi Minyak Terendah")
right_col.text(f"Nama Negara: {alst_1_neww2[aloio]}")
right_col.text(f"Kode Negara: {kodenega[aloio]}")
right_col.text(f"Region: {regioon[aloio]}")
right_col.text(f"Sub Region: {subregioon[aloio]}")
right_col.text(f"Produksi Terbesar: {alst_2_neww2[aloio]}")
ot = pd.read_csv('produksi_minyak_mentah.csv')
abssvn = ot[ot.kode_negara == kodenega[aloio]]
right_col.dataframe(abssvn)

st.subheader("Negara Dengan Produksi Minyak Nol")
aabbeeek = ot[ot.tahun == tahh4][ot.produksi == 0.0]
st.dataframe(aabbeeek)
