# program kasir sederhana
from data_barang import db
import pandas as pd
print("hello world")



def tampilkan_barang():
    print("\n=== Daftar Barang ===")
    print(pd.DataFrame(db).to_string(index=False))


def cari_barang(kode):
    for barang in db:
        if barang['kode'] == kode:
            return barang
    return None

def hitung_total(keranjang):
    total = 0
    for item in keranjang:
        print(item)
        total += item['harga'] * item['jumlah']
    return total

def cetak_struk(keranjang, total, bayar):
    print("\n=== STRUK PEMBELIAN ===")
    print("Nama Barang\tJumlah\tHarga\tTotal")
    print("-" * 50)
    for item in keranjang:
        print(f"{item['nama']}\t{item['jumlah']}\tRp {item['harga']:,}\tRp {item['harga']*item['jumlah']:,}")
    print("-" * 50)
    print(f"Total Belanja: Rp {total:,}")
    print(f"Bayar: Rp {bayar:,}")
    print(f"Kembalian: Rp {bayar-total:,}")

def main():
    keranjang = []
    
    while True:
        print("\n=== PROGRAM KASIR ===")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang ke Keranjang")
        print("3. Proses Pembayaran")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_barang()
            
        elif pilihan == "2":
            tampilkan_barang()
            kode = input("\nMasukkan kode barang: ").upper()
            barang = cari_barang(kode)
            
            # Jika barang ditemukan barang tidak bernilai None
            if barang:
                jumlah = int(input(f"Masukkan jumlah {barang['nama']}: "))
                item = {
                    'nama': barang['nama'],
                    'jumlah': jumlah,
                    'harga': barang['harga']
                }
                keranjang.append(item)
                print(f"\n{barang['nama']} sebanyak {jumlah} berhasil ditambahkan ke keranjang")
            else:
                print("\nBarang tidak ditemukan!")
                
        elif pilihan == "3":
            if not keranjang:
                print("\nKeranjang masih kosong!")
                # akan kembali ke awal loop
                continue
                
            total = hitung_total(keranjang)
            print(f"\nTotal belanja: Rp {total:,}")
            
            while True:
                bayar = int(input("Masukkan jumlah pembayaran: Rp "))
                if bayar >= total:
                    break
                print("Pembayaran kurang!")
            
            cetak_struk(keranjang, total, bayar)
            keranjang = []
            
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program ini!")
            break
            
        else:
            print("\nPilihan tidak valid!")

# Jalankan program
main()
