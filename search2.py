#시각 
#정수 N이 입력되면 3이 포함되는 경우를 count
#000000  1시59분59초 n 시 m 분 s 초 
n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1

print(count)