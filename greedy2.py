# n = input().split()
# n은 배열이다.2 4 5 => ['2', '4', '5']
# map 은 리스트의 요소를 지정된 함수로 변경...... map(적용시킬함수, 적용할 요소들)
# 6 6 6 5 / 6 6 6 5     k+1이 반복된다.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

b = 0
a = m // (k+1)
b = m % (k+1)

result = first* k * a + second * a + first * b

print(result)
