# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC ## Access Element
# MAGIC Keunikan lain dari looping dengan python adalah selain bahasa yang mudah dimengerti dalam looping, kita juga bisa mengakses elemen yang terdapat pada sebuah list. Berikut ini contohnya :
# MAGIC ``` javascript
# MAGIC #Tugas 3.2.1
# MAGIC count=[1,2,3,4,5] #elemen list
# MAGIC
# MAGIC for number in count: #looping untuk menampilkan semua elemen pada count
# MAGIC     print("Ini adalah element count : ", number) #menampilkan elemen list pada count
# MAGIC ```
# MAGIC Implekementasikan kode diatas, ketikan pada code cell di bawah ini, berikan penjelasan terkait kode diatas

# COMMAND ----------

# Jawaban Tugas 3.2.1
count=[1,2,3,4,5]
for number in count:
    print(" Ini adalah element count : ", number)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Tugas Praktek 3.2.2
# MAGIC 1. Buatlah sebuah program yang bisa mengeluarkan angka 1 sampai 10.
# MAGIC 1. Buatlah sebuah program yang bisa mengeluarkan angka -20 sampai -50.
# MAGIC 3. Tampilan akan menunjukan "Angka ganjil 1" untuk angka ganjil dan "Angka genap 2" untuk angka genap. (Menggunakan looping for)
# MAGIC
# MAGIC **Note:** Kode dasar sudah disertakan, Anda cukup mengganti tanda # dengan nilai-nilai yang sesuai.

# COMMAND ----------

#Jawaban Tugas 3.2.1.1
count=[1,2,3,4,5,6,7,8,9,10]

for number in count:
    print("Keluarkan angka 1 - 10 : ", number)

# COMMAND ----------

#Jawaban Tugas 3.2.1.2
for i in range(-20, -51, -1):
  print("Keluarkan angka dari (-20 sampai -50) angka", i)



# COMMAND ----------

#Jawaban Tugas 3.2.1.3
for i in range(1, 11):
  if i % 2 == 0:
    print(f"Angka genap {i}")
  else:
    print(f"Angka ganjil {i}")
