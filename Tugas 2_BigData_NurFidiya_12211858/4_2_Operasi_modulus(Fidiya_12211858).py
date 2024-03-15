# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC **Operasi modulus**
# MAGIC
# MAGIC Modulus memang jarang dipakai namun, dibeberapa kasus modulus sangat berguna untuk mempercepat proses perhitungan. Modulus sendiri merupakan fungsi yang akan menghitung sisa dari hasil pembagian. Untuk lebih jelasnya silahkan lakukan praktek di bawah ini :
# MAGIC ``` javascript
# MAGIC c=10
# MAGIC d=3
# MAGIC
# MAGIC modulus=c%d
# MAGIC print("Hasil modulus",modulus)
# MAGIC ```
# MAGIC Ketikan code cell di bawah ini pada editor:

# COMMAND ----------

##Jawaban Tugas Praktek 3.2
c=10
d=3

modulus=c%d
print("Hasil modulus",modulus)

# COMMAND ----------

# MAGIC %md
# MAGIC Kenapa modulus bisa seperti itu? (berikan jawaban anda pada cell teks diabawah ini)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Jawaban Keterangan 
# MAGIC karena modulus itu membagi sebuah bilangan tetapi menampilkan hasil sisa dari bagi tersebut, misal 4mod2, maka sisanya 0
# MAGIC lalu jika 5mod3 adalah 2
# MAGIC ....