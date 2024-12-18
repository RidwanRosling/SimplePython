# data_barang.py
import pandas as pd
daftar_barang = [
    {"kode": "B001", "nama": "Beras", "harga": 15000},
    {"kode": "M001", "nama": "Minyak Goreng", "harga": 20000},
    {"kode": "T001", "nama": "Telur", "harga": 28000},
    {"kode": "G001", "nama": "Gula", "harga": 12500},
    {"kode": "K001", "nama": "Kopi", "harga": 5000}
]

daftar_barang2 = {
    "kode" : ["","B001","M001","T001","G001","K001"],
    "nama" : ["","Beras","Minyak Goreng","Telur","Gula","Kopi"],
    "harga" : ["",15000,20000,28000,12500,5000]
}
data = [pd.DataFrame(daftar_barang2)['kode'].to_string(index=False)]
print (data)

for i in data:
    if data == "B001":
        return print ("1"):
    else none