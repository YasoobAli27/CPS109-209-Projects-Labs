#Yasoob Ali
#2019.09.24
#Quiz 3
#500953533
#Section 8

x = int(input('Enter an integer X:\n'))
y = int(input('Enter an integer Y:\n'))
result = 0
boolean = False

for n in range (y+1):
    while x <= y:
        if x > 1 :
            for i in range (2,x):
                if x % i == 0:
                    boolean = True
                    break
                boolean = False
        if boolean == False and x > 1:
            result = result + x
        x = x + 1

print("The sum of primes between ", x, "and ", y, "is:",result)
