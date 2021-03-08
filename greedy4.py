
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기

while True :
    if n % k != 0:
        result += n % k
        n -= n % k

    else :
        result += 1
        n //= k

    if n == 1 :
        break


print(result)