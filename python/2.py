a=1
b=2
x=0
total=0
while(b<4000000):
    if(b%2==0):
        total = total + b
    x = a
    a = b
    b = a + x
print(total)
