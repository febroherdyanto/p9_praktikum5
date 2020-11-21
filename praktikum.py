from prettytable import PrettyTable

print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI.20.B.1")
print("=======================")
print()
# Buat program sederhana yang akan menampilkan daftar nilai
# mahasiswa, dengan ketentuan
# • Program dibuat dengan menggunakan Dictionary
# • Tampilkan menu pilihan: (L)ihat, (T)ambah Data, (U)bah Data, (H)apus Data, (C)ari Data, (K)eluar
# • Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
# uts: 35%, uas: 35%)
# • Buat flowchart dan penjelasan programnya pada README.md.
# • Commit dan push repository ke github.
# Data untuk menambahkan : NIM, Nama, NIlai UTS, NIlai UAS, NIlai Tugas

daftar = {}


print("[ (L)ihat , (T)ambah, (U)bah, (C)ari, (K)eluar ]")
tanya = input("Masukkan Pilihan : ")
if tanya == "T":
    print("Tambah Data ")
    nim_v = input("NIM : ")
    nama_v = input("Nama Lengkap : ")
    uts_v = input("Nilai UTS : ")
    uas_v = input("Nilai UAS : ")
    tugas_v = input("Nilai Tugas : ")
    akhir_v = 0.3 * float(tugas_v) + 0.35 * float(uts_v) + 0.35 * float(uas_v)
    nim_k = nim_v[0:20]
    nama_k = nama_v[0:100]
    tugas_k = tugas_v[0:5]
    uts_k = uts_v[0:5]
    uas_k = uas_v[0:5]
    akhir_k = 0.3 * float(tugas_v) + 0.35 * float(uts_v) + 0.35 * float(uas_v)

    daftar = (nim_k, nama_k, tugas_k, uts_k, uas_k, akhir_k)
    print(daftar)

    print()
    print("==== Daftar Nilai ====")
    x = PrettyTable()
    i = 1
    # for data in range(daftar):
    x.field_names = ["No", "NIM", " NAMA", "TUGAS", "UTS", "UAS", "AKHIR"]
    x.add_row([i, daftar[0], daftar[1], daftar[2], daftar[3], daftar[4], daftar[5]])
    # x.add_row(["no.", data[0], data[1], data[2], data[3], data[4], data[5]])
    print(x)
elif tanya == "L":
    print("Menampilkan Semua Hasil")
elif tanya == "U":
    print("EDIT FILE")
elif tanya == "C":
    print("MENCARI RECORD")
elif tanya == "K":
    print("KELUAR")
else:
    print("PILIHAN ANDA SALAH")
