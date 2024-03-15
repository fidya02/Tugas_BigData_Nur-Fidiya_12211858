# Databricks notebook source
# MAGIC %md
# MAGIC ##Melakukan Comment Pada Python
# MAGIC Pada suatu kegiatan membuat code, penting sekali bagi para penulis codenya untuk memberikan sebuah dokumentasi pada penulisan codenya. Mengapa hal itu sangat penting? Sederhana, jika codenya sudah lebih dari ribuan baris dan ada beberapa bagian yang perlu diperbaiki karena suatu perubahan, para penulis code cukup melihat dokumentasinya dan tidak perlu membaca dan memahami seluruh isi code dari awal. Nah, salah satu metode yang biasa digunakan adalah menggunakan comment. Sama dengan Bahasa Python juga menggunakan tanda “#” untuk melakukan comment pada script.
# MAGIC
# MAGIC Cobalah ketikkan sebuah kalimat seperti di bawah ini beserta commentnya. Kemudian lakukan eksekusi dengan menekan tombol **[Run]**

# COMMAND ----------

print("Ini adalah sebuah baris kode")#ini adalah contoh comment dan tidak akan tercetak

# COMMAND ----------

# MAGIC %md
# MAGIC Perlu diketahui, comment tidak akan pernah tampil pada hasil melalui console atau GUI. Fungsi comment bisa dikatakan sebagai penanda. Kenapa bab ini diberikan diawal? Harapannya dengan pengetahuan ini setiap kali Anda membuat baris code, bisa diberikan dokumentasi. Dokumentasi sangat penting untuk pengembangan suatu code apabila memang nanti diperlukan.
# MAGIC
# MAGIC Dokumentasi kode juga berlaku untuk variable. Sangat penting mengetahui bahwa setiap variable berfungsi sebagai apa dan isinya apa. Maka dari itu jangan lupa untuk membuat dan memberi comment untuk setiap kode pada materi kita
# MAGIC
# MAGIC  
# MAGIC
# MAGIC **Tugas Praktek 3.2**
# MAGIC
# MAGIC 1. Berikan keterangan untuk setiap baris program dengan perintah comment

# COMMAND ----------

#Jawab Tugas Praktek 3.2 Nomor 1

print(10*2+5) #fungsi matematika
print("20") #fungsi mencetak kalimat

# COMMAND ----------

# MAGIC %md
# MAGIC 2. Cetak Nama dan NIM anda dilayar berikan comment untuk masing - masing perintah

# COMMAND ----------

#Jawab Tugas Praktek 3.2 Nomor 2
print('Nama  : Nur Fidiya')
print('NIM   : 12211858')
print(10*2+5) #fungsi matematika
print("20") #fungsi mencetak kalimat