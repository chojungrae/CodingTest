x = input()
y = input()

x = int(x)
y = int(y)

if x > 0 :
    print(1 if y > 0 else 4)
elif x < 0 :
    print(2 if y > 0 else 3)
else :
    print("{x},{y}".format(x=x, y=y))
