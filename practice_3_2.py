T = int(input())
list = []
for i in range(1, T+1) :
    A, B = map(int, input().split())
    list.append(A+B)

for i in range(0, len(list))  :
    print(str(list[i]))
