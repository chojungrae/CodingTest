import sys

T = int(input())
result = []
for _ in range(1, T+1) :
    a, b = sys.stdin.readline().rstrip("\n").split()
    result.append(int(a) + int(b))

for i in range(0, len(result)) :
    print(result[i])
