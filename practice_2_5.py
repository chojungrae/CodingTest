a, b = map(int, input().split())

print((a-(b<45))%24, (b-45)%60)
#
# if b - 45 >= 0  :
#     b -= 45
#     print(a, b)
# else :
#     b = (60 + b - 45)
#     if a == 0 :
#         a = 23
#     else :
#         a -= 1
#     print(a, b)
