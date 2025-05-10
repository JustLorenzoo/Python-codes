import re

def cek_teks(teks):
  """
  Mengecek apakah teks memenuhi kriteria berikut:
  - Panjang tepat 10 karakter.
  - Minimal memiliki 2 huruf besar.
  - Minimal memiliki 1 angka.

  Args:
    teks: String yang ingin dicek.

  Returns:
    True jika teks memenuhi semua kriteria, False jika tidak.
  """
  if len(teks) != 10:
    return False
  if len(re.findall(r'[A-Z]', teks)) < 2:
    return False
  if not re.search(r'\d', teks):
    return False
  return True

# Contoh penggunaan
input_teks = input("Buat password")
if cek_teks(input_teks):
  print("Password aman")
else:
  print("Password kurang aman")
