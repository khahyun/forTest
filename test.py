arr =  [[0]*19 for _ in range (19)]
n = int(input())
for i in range(n) :
  x, y = input().split()
  arr[int(x)-1][int(y)-1] = 1
  
for i in arr :
    for m in i:
        print(m, end=' ')
    print()