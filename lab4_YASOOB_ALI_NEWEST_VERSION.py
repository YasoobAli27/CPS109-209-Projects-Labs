#Syed Yasoob Ali
#500953533
#2019.10.10
#Lab 4 Programs


#1

#prints the statement 10 number of times
def helloWorld():
    print("Hello World")

for x in range(10):
    helloWorld()


#2

#takes in a string variable for the name and prints it
def helloName(username):
    print('Hello,',username)

#string is inputted by the user and then the function is called
abc = input('Please input a name: ')
helloName(abc)


#3

#function takes in 2 strings, 1 for first name and 1 for last name
def helloFullName(firstname,lastname):
    #reverses the order of the variables for the 2nd print
    print('Hello,',firstname,lastname)
    print('Hello,',lastname,firstname)

#both first name and last name are inputted by user and then the function is called
fn = input('Hello, please input a first name. ')
ln = input('And also input a last name. ')
helloFullName(fn,ln)


#4

#takes in a string variable and an integer variable
def repeatPhrase(phrase,n):
    # the first case has to be lower, so it will take the phrase inputted and convert it to lower
    # it then prints that phrase, for the first iteration of n and sets the state to lowercase
    phrase2 = phrase.lower()
    print(phrase2)
    isLower = True
    # since the first statement was already printed, the loop only goes up until n - 1 in order to remain accurate to the amount of times it should repeat
    for x in range(0,n-1):
        #if the previous sentence was lowercase, it will take the phrase and change it to uppercase and set isLower to false
        if isLower == True :
            phrase2 = phrase2.upper()
            print(phrase2)
            isLower = False
        # otherwise, it will make the sentence all lowercase and set isLower to true
        elif isLower == False :
            phrase2 = phrase2.lower()
            print(phrase2)
            isLower = True

#phrase and number of times its repeated is inputted by user
#function is then called 
string = input('Please enter a phrase.')
number = int(input('How many times do you want it to repeat.'))

repeatPhrase(string,number)


#5

#n is inputted by user to determine the timetable size
n = int(input('What size would you like your time table to be: '))
#function takes in integer value of n
def timesTable(n):
    #j is set to 1 by default and list is created to store all values
    j = 1
    List = []
    #creates an nested for-loop that will cycle through all values of the table, up until the length of n
    #it will then add all of these values to a list which gets printed and then cleared to make room for the next set of values to be printed
    for i in range(n):
        for j in range(n):
            List.append((i+1)*(j+1))
        print(List)
        List.clear()

timesTable(n)


#6

#x in inputted by the user to determine if that value is a perfect cube
x = int(input('Please input an integer value: '))
#takes in integer value of x
def perfectCube(x):
    #sets m to 0 initially
    #when m to the power of 3 is not equal to the absolute value of x, that means that m is not the value of the cube root
    #will increase m by 1 each time if m^3 is lower than x in order to get closer to the value that it should be
    #at the end of the loop (once m^3 is larger than absolute x), it will return either true or false depending on if m^3 is equal to absolute x
    #if it is, then it will return true, otherwise it will return false indicating that x is not a perfect cube.
    m = 0
    while m ** 3 < abs(x):
        m = m + 1
    if m ** 3 != abs(x) :
        return False
    else :
        #it will also first check to see if the user inputted a negative value for x.
        #if so, it will change m to -m
        if x < 0 :
            m = -m
        return True

#prints the result depending on value of x
if perfectCube(x) == True :
    print('Yes, its a perfect cube.')
else :
    print('No, its not a perfect cube.')



#7

    
#function will run without any inputs required until midway through the function
def biggestOdd() :
    #creates an empty list and an integer variable initially set to 0
    #n is also created, initially set to 1 so that the while loop will run immediatly
    List = []
    largestOddNumber = 0
    n = 1
    #while loop will request user input to keep entering numbers until they enter 0
    #entering 0 indicates that they are done listing values to be checked and breaks from the while loop
    while n != 0 :
        n = int(input('Please enter a number'))
        if n == 0:
            break
        #it will also add every value inputted to the list and print it back to the user 
        List.append(n)
        print(List)
    #after the while loop is finished, it will then cycle through a for loop to check if all the numbers in the list are odd
    #if any of these numbers are odd AND they are greater than the current largest number, then it will set that number to the new largestOddNumber
    for x in range(len(List) - 1):
        if List[x] % 2 == 1 and List[x] > largestOddNumber :
            largestOddNumber = List[x]
    return largestOddNumber

#creates a new variable that calls the function and sets itself to the largest odd number
#if all numbers are even, then this value will be user as that is what LargestOddNumber is set to at the beginning.
z = biggestOdd()
#prints largest odd number or declares there to be none.
if z == 0 :
    print('All numbers are even.')
else :
    print(z,'is the largest odd number.')



#8

#creates function that takes in 1 string value
def biggestBuried(x) :
    #sets the base value of num to nothing and the current largestNumber to 0
    num = ''
    largestNumber = 0
    #creates a for loop that cycles through all values of the string inputted
    for i in x :
        #ascii values from 0-9 (48 is 0, 57 is 9)
        #if i is within this range of values, that means it is a digit and will then check the next number to see if its also a digit in order to combine them
        if i >= chr(48) and i <= chr(57) :
            num += i
        #otherwise, if it is a digit and the value that it is currently on is largest than the largestNumber, then it will make largestNumber that value
        #and reset num to nothing, as it will move on to the next part of the string
        elif num.isdigit() == True and int(num) > largestNumber :
            largestNumber = int(num)
            num = ''
        #otherwise, it is not a digit and will be ignored
        else :
            num = ''
    #after the for loop is complete, it will repeat the following if statement to ensure that the largestNumber is still the highest value buried in the string
    if num.isdigit() == True and int(num) > largestNumber :
        largestNumber = int(num)
    #will return the largestNumber value
    return largestNumber

print(biggestBuried('abcd51kkk3kk19ghi')) 
print(biggestBuried('kkk32abce@@-33bb14zzz'))
print(biggestBuried('this15isast22ring-55'))



#9

#creates function that takes in 2 integer values 
def squareRoot(x, epsilon):
    #low is set to 0 by default and high is set to the value inputted by user
    #y value is the first guess, and will be halfway between high and low
    low = 0
    high = x
    y = (low + high) / 2
    #while loop will continue to cycle through until y^2 - x is less than the inputted epsilon value (which determines how accurate you want the answer to be)
    #as this loop runs, it will set the high or low value to the current y, depending on the value of y (based on if the guess is too high or too low from the real answer)
    while (abs(y ** 2 - x) > epsilon):
        if y ** 2 > x :
            high = y
        if y ** 2 < x :
            low = y
        #will also reset y to the halfway point between the new high and low values and prints the guess
        y = (low + high) / 2
        print('guess = ',y)
    print(y, 'is close enough to:',x)

#sets 2 integer variables based on user input
xint = int(input('Please input an integer value: '))
epsi = float(input('Please input your epsilon: '))

#calls the function and uses the 2 user inputs for x integer and epsilon.
squareRoot(xint,epsi)


#10

#creates an integer value based on user input 
n = int(input('Please enter a decimal number to convert to binary.'))
#creates function that takes in the user's integer input
def decimalToBinary(n) :
    #creates a blank list to store values
    List = []
    #while loop will run only when n is greater than 0
    #n will continue to be divided by 2 (uses // so it will round to nearest whole number and save the remainder)
    #eventually, n will reach 0, which means its done dividing the decimal number by 2 and is ready to print the binary value
    while n != 0 :
        List.append(n%2)
        n = n//2
    #takes the list of binary bits and reverses it so it is in the correct order
    #prints that list
    List.reverse()
    print(List)

#calls the function and makes it take in the user's inputted decimal number.
decimalToBinary(n)








