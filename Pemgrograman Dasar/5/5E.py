# satuan, puluhan, ribuan, etc.

a = int(input(''))
if (a <= 9 and a > 0):
    print('satuan')
elif (a <= 99) and a > 0:
    print('puluhan')
elif (a <= 999 and a > 0):
    print('ratusan')
elif (a <= 9999 and a > 0):
    print('ribuan')
elif (a <= 99999 and a > 0):
    print('puluhribuan')