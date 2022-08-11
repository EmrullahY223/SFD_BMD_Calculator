# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:20:23 2021

@author: Emrullah
"""
# kiriş_uzunluğu = int(input("Kiriş uzunluğu")) 

# Gereken verileri al

kuvvet_sayısı = int(input("Kuvvetlerin sayısı:"))

kuvvet_konum_listesi = [[float(f_l)for f_l in input("önce kuvvet sonra konum (Aralarında boşluk bırak):").split()]for i in range(kuvvet_sayısı)]
print(kuvvet_konum_listesi)

destek1_kon = float(input("birinci desteğin konumu:"))

destek2_kon = float(input("ikinci desteğin konumu:"))


# Statik denge koşulu ile kuvvetleri hesapla

def tepki_hesabı(kuvvet_konum,destek1,destek2):
    destek2_kuvvet = 0.0
    destek1_kuvvet = 0.0
    kuvvet_toplam = 0.0
    
    for kuvvet_k in kuvvet_konum:
        
        destek2_kuvvet += -(kuvvet_k[0]*(kuvvet_k[1]-destek1))/(destek2-destek1)
        #print (destek2_kuvvet)
        kuvvet_toplam -= kuvvet_k[0]
    destek1_kuvvet = kuvvet_toplam - destek2_kuvvet
    
    
    
    return destek1_kuvvet,destek2_kuvvet

tepki1,tepki2 = tepki_hesabı(kuvvet_konum_listesi,destek1_kon,destek2_kon)

print(f" tepki1 = {tepki1}\n tepki2 = {tepki2}")