# Import modul data_barang yang berisi daftar barang
from data_barang import daftar_barang

def tampilkan_barang():
    print("\n=== Daftar Barang ===")  # Mencetak judul
    print("Kode\tNama\t\tHarga")      # Mencetak header tabel
    print("-" * 30)                    # Mencetak garis pembatas
    # Loop untuk menampilkan setiap barang
    for barang in daftar_barang:
        print(f"{barang['kode']}\t{barang['nama']}\t\tRp {barang['harga']:,}")

def cari_barang(kode):
    # Loop untuk mencari barang berdasarkan kode
    for barang in daftar_barang:
        if barang['kode'] == kode:
            return barang    # Mengembalikan data barang jika ditemukan
    return None             # Mengembalikan None jika tidak ditemukan

def hitung_total(keranjang):
    total = 0
    # Loop untuk menghitung total harga
    for item in keranjang:
        total += item['harga'] * item['jumlah']
    return total

def cetak_struk(keranjang, total, bayar):
    print("\n=== STRUK PEMBELIAN ===")
    print("Nama Barang\tJumlah\tHarga\tTotal")
    print("-" * 50)
    # Loop untuk mencetak setiap item di keranjang
    for item in keranjang:
        print(f"{item['nama']}\t{item['jumlah']}\tRp {item['harga']:,}\tRp {item['harga']*item['jumlah']:,}")
    print("-" * 50)
    # Mencetak ringkasan pembayaran
    print(f"Total Belanja: Rp {total:,}")
    print(f"Bayar: Rp {bayar:,}")
    print(f"Kembalian: Rp {bayar-total:,}")

def main():
    keranjang = []     # Inisialisasi keranjang kosong
    
    while True:        # Loop utama program
        # Menampilkan menu
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
            
            if barang:
                # Jika barang ditemukan, minta jumlah dan tambahkan ke keranjang
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
                continue
                
            total = hitung_total(keranjang)
            print(f"\nTotal belanja: Rp {total:,}")
            
            # Loop untuk memastikan pembayaran cukup
            while True:
                bayar = int(input("Masukkan jumlah pembayaran: Rp "))
                if bayar >= total:
                    break
                print("Pembayaran kurang!")
            
            cetak_struk(keranjang, total, bayar)
            keranjang = []  # Reset keranjang setelah transaksi
            
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program ini!")
            break
            
        else:
            print("\nPilihan tidak valid!")

# Memastikan program hanya dijalankan jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()