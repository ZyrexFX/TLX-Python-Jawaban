# floor, ceil

a = float(input(''))
m = int(a)

if (a == m):
    print(m, m)
elif (a >= 0):
    f = int(a) // 1
    c = int(a) // 1 + 1
    print(f, c)
elif (a <= 0):
    f = int(a) // 1 - 1
    c = int(a) // 1
    print(f, c)