# Databricks notebook source
# MAGIC %md
# MAGIC ##3.1. Tugas:
# MAGIC Berikut ini adalah psudo code  untuk melakukan pengecekan bertingkat
# MAGIC ``` javascript
# MAGIC i <= 2
# MAGIC IF i < 7 THEN
# MAGIC 	CETAK "Nilai i kurang dari 7"
# MAGIC 	IF i < 3 THEN
# MAGIC 	   CETAK "Nilai i kurang dari 7 dan kurang dari 3"
# MAGIC 	ELSE
# MAGIC 		CETAK "Nilai i kurang dari 7 tapi kurang dari 3"
# MAGIC
# MAGIC ```
# MAGIC Implekementasikan kode diatas dalam kode python. Ketikan code cell di bawah ini pada editor:

# COMMAND ----------

##Jawaban Tugas 3.1
i = 2

if i <= 2:
    print("Nilai i kurang dari 7")
    if i < 3:
        print("Nilai i kurang dari 7 dan kurang dari 3")
    else:
        print("Nilai i kurang dari 7 tapi tidak kurang dari 3")
