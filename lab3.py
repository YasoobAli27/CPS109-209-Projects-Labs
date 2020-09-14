# Yasoob Ali
# 2019.09.24
# Lab 3, 10 programs
# All of the code is commented out to prevent it from all running at the same time. Please uncomment out 1 program at a time, when you test them.

#Program 1

#n = int(input('Enter a Number '))
#for guess in range (abs(n)) :
#    if guess ** 4 >= n :
#        break
#if guess ** 4 != abs(n) :
#    print('no perfect 4th root for ',n)
#else :
#    if n < 0 :
#        guess = -guess
#    print(guess, 'is the 4th root of ', n)



#Program 2

#n = int(input('Enter a Number '))
#AN = abs(n)

#power = 2
#while power < 6 :
#    root = 0
#    while root ** power < AN :
#        root = root + 1
#    if root ** power == n :
#        if n < 0 and power % 2 == 1 :
#            root = -root
#            print(root, 'to the power of', power, 'is', n)
#            break
#        else :
#            print(root, 'to the power of', power, 'is', n)
#            break
#        power = power + 1
#if power == 6 :
#    print ('Did not find a value root and power for ', n)



#Program 3


#n = int(input('Enter a Number '))
#AN = abs(n)

#root = 2
#while root < 6 :
#    power = 1
#    while root ** power < AN :
#        power = power + 1
#    if root ** power == n :
#        if n < 0 and power % 2 == 1 :
#            root = -root
#            print(root, 'to the power of', power, 'is', n)
#            break
#        else :
#            print(root, 'to the power of', power, 'is', n)
#            break
#        root = root + 1
#if power > 6 :
#    print ('Did not find a value root and power for ', n)



#Program 4

#n = int(input('Enter a Number '))
#p = input('Enter a phrase ')

#while n > 0 :
#    print(p)
#    n = n - 1



#Program 5

#i = 0
#n = 0
#highestOdd = 0

#for i in range (10) :
#    n = int(input('Enter A Number'))
#    if (n % 2 == 1) :
#        if (n > highestOdd) :
#            highestOdd = n
#print('The highest odd number is',highestOdd)



#Program 6 

#string = str(input("Please input a string containing numbers: "))
#sum = 0
#for s in string :
#    if s.isdigit() == True:
#        n = int(s)
#        sum = sum + n
#print("The sum of numbers in the string is: ", sum)




#Program 7

#decimals = input('Enter a set of numbers containing decimal numbers. Please seperate these numbers with commas: ')
#totalValue = 0
#for n in decimals.split(","):
#    totalValue = totalValue + float(n)
#print(totalValue)




#Program 8

#n = 0

#while n <= 0 :
#    n = int(input('Please Enter A Positive Number'))
#print('done')

#epsilon = 0.01
#guess = n/2.0
#while abs(guess*guess - n) >= epsilon :
#    guess = guess - (((guess**2) - n)/(2*guess))
#print('Square Root of', n, 'is about', guess)



#Program 9

#k = int(input('Please enter a number'))

#guess = k / 2
#error = guess ** 3 - k
#epsilon = 0.01
#while abs(error) > epsilon:
#    guess = guess - (error) / (k * guess ** 2)
#    error = guess ** 3 - k
#print('Approximate cube root of', k, 'is', round(guess,3))



#Program 10

#n = 0
#List = []
#binary = []

#while n <= 0 :
#    n = int(input('Please enter a positive number.'))
#while n > 0 :
#    r = n % 2
#    n = n // 2
#    List.append(r)
#print(List)
#for i in range (len(List) - 1,-1,-1):
#     z = List.pop(i)
#     binary.append(z)
#print(binary)

    



















