# Databricks notebook source
# MAGIC %md
# MAGIC **Praktek Operasi Input Dan Operator Matematika**
# MAGIC
# MAGIC Bukalah kembali praktek operator matematika.
# MAGIC
# MAGIC Ubahlah agar variable **a** dan **b** menggunakan input dari keyboard
# MAGIC
# MAGIC
# MAGIC Implementasikan code di bawah ini pada kode cell editor:
# MAGIC ``` javascript
# MAGIC selisih = a-b
# MAGIC jumlah = a+b
# MAGIC kali = a*b
# MAGIC bagi = a/b
# MAGIC print("Hasil penjumlahan dan b adalah", jumlah)
# MAGIC print("Selisih a dan b adalah :",selisih)
# MAGIC print("Hasil perkalian a dan b adalah :",kali)
# MAGIC print("Hasil  pembagian a dan b adalah:",bagi)
# MAGIC
# MAGIC ``` 
# MAGIC  
# MAGIC
# MAGIC Ketikan pada code cell di bawah ini pada editor:

# COMMAND ----------

##Jawaban Tugas Praktek 3.4
# Mendapatkan input dari keyboard
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

# Melakukan operasi matematika
selisih = a - b
jumlah = a + b
kali = a * b
bagi = a / b

# Menampilkan hasil
print("Hasil penjumlahan {} dan {} adalah {}".format(a, b, jumlah))
print("Selisih {} dan {} adalah {}".format(a, b, selisih))
print("Hasil perkalian {} dan {} adalah {}".format(a, b, kali))
print("Hasil pembagian {} dan {} adalah {}".format(a, b, bagi))
