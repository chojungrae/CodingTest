# list1 = list(map(int, input().split(" ")))
# list2 = list(map(int, input().split(" ")))

list1 = list(input())
list2 = list(input())

result3 = 0
result = 0
N = len(list1)
arrCnt = 0
for value1 in list2[::-1] :
    cnt = 0
    for value2 in list1[::-1] :
        s = str(int(value1) * int(value2))
        if(cnt == 0) :
            result3 += int(s)
        else :
            result3 += int(s) * (10 ** cnt)
        cnt += 1
        if(cnt == N) :
            result += result3  * (10 ** arrCnt)
            result3 = 0
    arrCnt += 1
print(result)
