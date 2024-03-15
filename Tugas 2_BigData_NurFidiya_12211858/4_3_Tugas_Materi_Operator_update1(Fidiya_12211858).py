# Databricks notebook source
# MAGIC %md
# MAGIC ##Tugas Praktek
# MAGIC ``` javascript
# MAGIC if ... :
# MAGIC     print("angka termasuk bilangan genap")
# MAGIC else:
# MAGIC     print("angka termasuk bilangan ganjil")
# MAGIC ``` 
# MAGIC Buatlah sebuah program yang bisa menentukan suatu nilai pada variable itu genap atau ganjil! Lakukan percobaan dengan langkah berikut:
# MAGIC
# MAGIC Buat variabel dengan nama “angka” isi dengan nilai 10
# MAGIC Ganti bagian … dengan perhitungan untuk menentukan angka modulus 2 bernilai 0.
# MAGIC
# MAGIC 1.   Buat variabel dengan nama **“angka”** isi dengan nilai 10
# MAGIC 2.   Ganti bagian … dengan perhitungan untuk menentukan angka modulus 2 bernilai 0.
# MAGIC
# MAGIC
# MAGIC Cek apakah benar dia bernilai genap maka keluarkan **"angka termasuk bilangan genap"**, jika sudah ganti nilai variable angka dengan nilai 5 cek lagi apakah dia bernilai ganjil dan keluarkan **"angka termasuk bilangan ganjil"**.
# MAGIC
# MAGIC Note: Anda bisa menggunakan materi-materi sebelumnya dengan menggabungkannya di tugas praktek ini untuk membantu anda dalam mengerjakan.
# MAGIC
# MAGIC
# MAGIC Ketikan pada code cell di bawah ini pada editor:

# COMMAND ----------

##Jawaban Tugas Praktek 3.3
# Buat variabel dengan nama "angka" dan isi dengan nilai 10
angka = 12

# Periksa apakah angka modulus 2 bernilai 0
if angka % 2 == 0:
  # Jika ya, cetak "angka termasuk bilangan genap"
  print("angka termasuk bilangan genap")

# Ubah nilai variabel "angka" menjadi 5
angka = 5

# Periksa apakah angka modulus 2 bernilai 0
if angka % 2 == 0:
  # Jika ya, cetak "angka termasuk bilangan genap"
  print("angka termasuk bilangan genap")
else:
  # Jika tidak, cetak "angka termasuk bilangan ganjil"
  print("angka termasuk bilangan ganjil")
