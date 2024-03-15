# Databricks notebook source
# MAGIC %md
# MAGIC ##Mencetak Tipe Data
# MAGIC **Praktik 2.4.1**
# MAGIC Cobalah mengetik kode di bawah ini :
# MAGIC ``` javascript
# MAGIC #tipe data Boolean
# MAGIC print(True)
# MAGIC
# MAGIC
# MAGIC #tipe data String
# MAGIC print("Mari belajar Python")
# MAGIC print('Belajar Python Sangat Dengan Mudah')
# MAGIC
# MAGIC
# MAGIC #tipe data Integer
# MAGIC print(20)
# MAGIC
# MAGIC
# MAGIC #tipe data Float
# MAGIC print(3.14)
# MAGIC
# MAGIC
# MAGIC #tipe data List
# MAGIC print([1,2,3,4,5])
# MAGIC print(["satu", "dua", "tiga"])
# MAGIC
# MAGIC
# MAGIC #tipe data Tuple
# MAGIC print((1,2,3,4,5))
# MAGIC print(("satu", "dua", "tiga"))
# MAGIC
# MAGIC
# MAGIC #tipe data Dictionary
# MAGIC print({"nama":"Budi", 'umur':20})
# MAGIC
# MAGIC #tipe data Dictionary dimasukan ke dalam variabel biodata
# MAGIC biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
# MAGIC print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
# MAGIC type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>
# MAGIC ``` 

# COMMAND ----------

#Jawab Praktik 2.4.1
#tipe data Boolean
print(True)


#tipe data String
print("Mari belajar Python")
print('Belajar Python Sangat Dengan Mudah')


#tipe data Integer
print(20)


#tipe data Float
print(3.14)


#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])


#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))


#tipe data Dictionary
print({"nama":"Budi", 'umur':20})

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>

# COMMAND ----------

# MAGIC %md
# MAGIC **Tugas Praktek 3.3**
# MAGIC
# MAGIC 1.Printing Data type menggunakan Variable.
# MAGIC Ketikan kode di bawah ini pada Code Editor.
# MAGIC ``` javascript
# MAGIC var_string="Mari Belajar Python"
# MAGIC var_int=10
# MAGIC var_float=3.14
# MAGIC var_list=[1,2,3,4]
# MAGIC var_tuple=("satu","dua","tiga")
# MAGIC var_dict={"nama":"Ali", 'umur':20}
# MAGIC
# MAGIC
# MAGIC print(var_string)
# MAGIC print(var_int)
# MAGIC print(var_float)
# MAGIC print(var_list)
# MAGIC print(var_tuple)
# MAGIC print(var_dict)
# MAGIC ```
# MAGIC

# COMMAND ----------

#Jawab Tugas Praktek 3.3 Nomor 1
var_string="Mari Belajar Python"
var_int=10
var_float=3.14
var_list=[1,2,3,4]
var_tuple=("satu","dua","tiga")
var_dict={"nama":"Fidiya", 'umur':21}


print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

# COMMAND ----------

# MAGIC %md
# MAGIC 2. Tambahkan code di bawah ini untuk mengetahui type data dari suatu value di variabel.
# MAGIC ``` javascript
# MAGIC print(type(var_string))
# MAGIC print(type(var_int))
# MAGIC print(type(var_float))
# MAGIC print(type(var_list))
# MAGIC print(type(var_tuple))
# MAGIC print(type(var_dict))
# MAGIC ```

# COMMAND ----------

#Jawab Tugas Praktek 3.3 Nomor 2
print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))