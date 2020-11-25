# Pertemuan 9 - Praktikum 5 *(repo: p9_praktikum5)*
Tugas Pertemuan 9 - Praktikum 5 (Bahasa Pemrograman)
<hr>

=========================<br>
= Nama  : Febro Herdyanto<br>
= NIM   : 312010043<br>
= Kelas : TI.20.B.1<br>
=========================<br>

Pada mata kuliah Bahasa Pemrograman - Pertemuan 9 kali ini saya mendapatkan materi *List, Tuple dan Dictionary*.<br>
Nah, untuk praktikum 5 ini materi yang didapatkan adalah **List**.<br>
<br>
* Didalam materi praktikum 5 ini terdapat 2 tugas. Yaitu : Latihan dan Praktikum.<br>

## Praktikum 5 - Latihan

* Berikut adalah tugas dari Latihan, bisa dilihat pada gambar dibawah ini :<br>
![Soal Tugas Latihan](pict/soal_latihan.PNG)<br>
* Berikut jawaban / *source code* / program sederhana yang telah saya buat :<br>
``` python
print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI.20.B.1")
print("=======================")
print()

kontak = {"Ari": "085215565501", "Dina": "08788767778"}
print("Nama | Nomor Telepon")
print("Menampilkan Dictionary Kontak")
print(kontak)
print("----------------------------------------------")
print("Menampilkan Kontak Ari")
print(kontak['Ari'])
print("----------------------------------------------")
print("Menambahkan kontak baru dengan nama Riko - 087654544")
kontak['Riko'] = '087654544'
print(kontak['Riko'])
print("----------------------------------------------")
print("Ubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print(kontak['Dina'])
print("----------------------------------------------")
print("Tampilkan semua Nama")
print(kontak.keys())
print("----------------------------------------------")
print("Tampilkan semua Nomor")
print(kontak.values())
print("----------------------------------------------")
print("Tampilkan daftar nama dan nomor")
print(kontak.items())
print("----------------------------------------------")
print("Hapus kontak Dina")
del kontak['Dina']
print(kontak)
```

* Untuk hasil dari source code tersebut adalah seperti berikut : <br>
![Jawaban Soal Latihan](pict/jawab_latihan.PNG)<br>

## Praktikum 5 - Praktikum

Untuk tugas yang kedua yaitu Tugas Praktikum, yaitu tugas untuk membuat program sederhana menampilkan Data Nilai Mahasiswa.<br>
* Berikut soal yang diberikan oleh dosen :<br>
![Soal Praktikum](pict/soal_praktikum.PNG)<br>

* Hasil yang diingkan oleh dosen, seperti ini :<br>
![Keinginan Dosen dari Soal Praktikum - 1](pict/ingin1.PNG)<br>

* Dan seperti ini :<br>
![Keinginan Dosen dari Soal Praktikum - 1](pict/ingin2.PNG)<br>

