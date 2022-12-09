# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:02:38 2022

@author: jovita amanda putri
"""

def cari_posisi(angka, cari, bawah, atas):
    if atas >= bawah:
        tengah = bawah + (atas - bawah)//2
        if angka[tengah] == cari:
            return tengah
        elif angka[tengah] > cari:
            return cari_posisi(angka, cari, bawah, tengah-1)
        else:
            return cari_posisi(angka, cari, tengah+1, atas)
    else:
        return -1

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
print(angka)
B_sort(angka)
print("\nSetelah disortir : ")
print(angka)
cari = int(input("\nMasukkan angka yang ingin dicari : "))
hasil = cari_posisi(angka, cari, 0, len(angka)-1) + 1
if hasil != -1:
    print("\nAngka yang dicari berada di posisi ke-" + str(hasil))
else:
    print("\nAngka tidak dapat ditemukan")