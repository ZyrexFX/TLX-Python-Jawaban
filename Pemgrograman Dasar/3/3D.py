# Format Masukan
# Sebuah baris berisi dua buah bilangan bulat N dan M.

# Format Keluaran
# Baris pertama berisi masing-masing A, dengan A adalah banyaknya bebek yang diberikan kepada masing-masing temannya. Baris kedua berisi bersisa B, dengan B adalah banyaknya sisa bebek Pak Dengklek.

a, b = input('').split()
c = int(a) // int(b)
mod = int(a) % int(b)
print('masing-masing ', c)
print('bersisa ', mod)