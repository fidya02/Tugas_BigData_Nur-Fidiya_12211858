# Databricks notebook source
# MAGIC %md
# MAGIC **Soal 5.1.1**
# MAGIC
# MAGIC Berikut ini adalah potongan kode implementasi fungsi *luas_limas_segi_empat()*
# MAGIC ``` javascript
# MAGIC print("Luas : %d" % luas_limas_segi_empat(Alas_limas, Tinggi_limas))​
# MAGIC ```
# MAGIC Lengkapilah kode tersebut dengan merancang sebuah fungsi agar bisa diimplementasikan sesuai dengan statment potongan kode diatas.
# MAGIC dengan mengetikan pada code cell di bawah ini pada editor.

# COMMAND ----------

def luas_limas_segi_empat(Alas_limas, Tinggi_limas):
  """
  Menghitung luas limas segiempat.

  Args:
    Alas_limas: Luas alas limas segiempat.
    Tinggi_limas: Tinggi limas segiempat.

  Returns:
    Luas limas segiempat.
  """

  Luas_selimut = (Alas_limas * Tinggi_limas) / 2
  Luas_limas = Alas_limas + Luas_selimut
  return Luas_limas

# Contoh penggunaan
s = int(input("Masukkan nilai sisi: "))
Alas_limas = s*s
Tinggi_limas = int(input("Masukkan tinggi limas: "))

luas = luas_limas_segi_empat(Alas_limas, Tinggi_limas)

print("Luas limas segiempat dengan alas {} dan tinggi {} adalah {}".format(Alas_limas, Tinggi_limas, luas))
