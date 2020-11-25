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

daftar = []
x = PrettyTable()

while True:
    print("[ (L)ihat , (T)ambah, (U)bah, (C)ari, (K)eluar ]")
    tanya = input("Masukkan Pilihan : ")
    if tanya == "L":
        print("==== Daftar Nilai ====")
        i = 0
        for data in daftar:
            i += 1
            x.field_names = ["No", "NIM", " NAMA", "TUGAS", "UTS", "UAS", "AKHIR"]
            x.add_row([i, data["nim"], data["nama"], data["tugas"], data["uts"], data["uas"], data["akhir"]])
        print(x)
    elif tanya == "T":
        print("Tambah Data ")
        nim_v = input("NIM : ")
        nama_v = input("Nama Lengkap : ")
        uts_v = input("Nilai UTS : ")
        uas_v = input("Nilai UAS : ")
        tugas_v = input("Nilai Tugas : ")
        akhir_v = 0.3 * float(tugas_v) + 0.35 * float(uts_v) + 0.35 * float(uas_v)
        daftar.append({"nim": nim_v, "nama": nama_v, "tugas": tugas_v, "uts": uts_v, "uas": uas_v, "akhir": akhir_v})
        print()
        print("==== Daftar Nilai ====")
        i = 0
        for data in daftar:
            i += 1
            x.field_names = ["No", "NIM", " NAMA", "TUGAS", "UTS", "UAS", "AKHIR"]
            x.add_row([i, data["nim"], data["nama"], data["tugas"], data["uts"], data["uas"], data["akhir"]])
        print(x)
        print(daftar)
    elif tanya == "U":
        print("EDIT FILE")
        print("Data siapa yang akan diubah ?")
        siapa = input("Masukkan NIM Mahasiswa yang akan diubah : ")

        print("Data apa yang akan diubah ? : ")
        mhs = input(" 1. Nama \n 2. Nilai Tugas \n 3. Nilai UTS \n 4. Nilai UAS\n Pilih dengan angka (1/2/3/4) : ")
        if mhs == "1":
            ubahnama = input("Silahkan masukan nama yang benar : ")
            for data in daftar:
                data[mhs] = ubahnama
                print(data.items())
        else:
            print("Data kosong")

    elif tanya == "H":
        print("HAPUS DATA")
    else:
        print("ANDA MEMILIH PILIHAN YANG SALAH")
