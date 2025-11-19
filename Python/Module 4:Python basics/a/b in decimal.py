limit = 10000
cntr = 0
a = 10108891
b = 7738383
print(a//b,'.', end='')
a = a % b
a *= 10
while True:
    print(a//b, end = '')
    a = a % b
    a = a * 10
    cntr = cntr + 1
    if cntr >= limit:
        break
