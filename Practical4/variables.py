a = 15           
b = 75
c = a + b
d = 90
e = 5
f = d + e
if c > f:
    print("c is longer than f,driving is quicker")
elif c == f:
    print("c is equal to f")
else:
    print("c shorter than f,bus is quicker")


for X in (True, False) :
    for Y in (True, False) :
        W= X and Y
        print(X,"and",Y,"=",W)