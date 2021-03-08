n = 1260
a = n // 500
b = (n - a * 500) // 100
c = (n - 500* a - 100*b)//50
d = (n - 500*a - 100*b - 50* c)//10

count = a+b+c+d
print(count)

count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)


