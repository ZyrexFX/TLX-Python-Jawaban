# jarak manhattan

# Format Masukan
# Sebuah baris berisi empat buah bilangan bulat x1, y1, x2, dan y2.

# Format Keluaran
# Sebuah baris berisi sebuah bilangan bulat yang merupakan jarak Manhattan dari kedua titik tersebut.

# Contoh Masukan
# -1 -1 1 1
# Contoh Keluaran
# 4

x1, y1, x2, y2 = input('').split()

selisihX = int(x1) - int(x2)
selisihY = int(y1) - int(y2)
jarak = abs(selisihX) + abs(selisihY)
print(jarak)