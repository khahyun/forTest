# 숫자 카드 게임
#리스트에 요소 추가(append)

n, m = map(int, input().split())
arr = []
new = []

for i in range(n) :
    a = list(map(int, input().split()))
    new.append(min(a))
    arr.append(a)

print(max(new))

