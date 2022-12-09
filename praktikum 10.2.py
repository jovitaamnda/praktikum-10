# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:56:26 2022

@author: jovita amanda putri
"""

def data_list(n=0,data=[],i=1):
    if (n == 0):
        return 0
    else : 
        isi = int(input("Masukkan angka ke-" + str(i) + " : "))
        data.append(isi)
        if(n == 1):
            return data
        else:
            i += 1
            return data_list(n-1,data,i)

def B_sort(angka):
  for i in range(len(angka)):    
    for n in range(0, len(angka) - i - 1):
      if angka[n] > angka[n + 1]:
        x = angka[n]
        angka[n] = angka[n+1]
        angka[n+1] = x


jumlah = int(input("Berapa banyak angka yang ingin di list : "))
angka = data_list(n = jumlah)
print("\nSebelum disortir : ")
print(angka)
B_sort(angka)
print("\nSetelah disortir : ")
print(angka) 