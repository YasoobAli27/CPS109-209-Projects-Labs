#EXAM PRACTICE

#Question 1
#My Solution
'''
def q1(a,b,c,epsilon):
    numMax = a
    numMin = a
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)

    for i in range(len(numList)):
        if numMax < numList[i]:
            numMax = numList[i]
        if numMin > numList[i]:
            numMin = numList[i]

    print(numMax, numMin)
    if (numMax - numMin) <= epsilon:
        return(True)
    else:
        return(False)

print(q1(5,6,7,2))
'''
#Question 1
#Harley's Solution
'''
def q1(a,b,c,epsilon):
    return max(a,b,c) - min(a,b,c) <= epsilon
    pass

print(q1(5,6,7,2))
'''
#Question 2
#My Solution
'''
def q2(n):
    numMin = n
    numMax = n*3
    numSum = 0

    while numMax >= numMin:
        if numMax % 2 == 1:
            numSum += numMax
        numMax -= 1
    return numSum

print(q2(4))
'''
#Question 2
#Harley's Solution
'''
def q2(n):
    sum = 0
    for i in range(n,3*n + 1):
        if i % 2 == 1:
            sum += i
    return sum
    pass

print(q2(2))
'''
#Question 3
#Harley's Solution [Skipped My Solution]
'''
def q3(x,epsilon):
    guess = x / 2
    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess
    pass

print(q3(99,0.1))
'''
#Question 4
#Harley's Solution [Same As My Solution]
'''
def q4(s):
    finalString = ''

    for i in range(len(s)):
        finalString += i * s[i]

    return finalString

print(q4('dogfo'))
'''
#Question 5
#Harley's Solution [Same As My Solution]
'''
def q5(sentence):
    words = sentence.split()
    result = []
    for word in words:
        word.replace('.','')
        word.replace(',','')
        word.replace('!','')
        word.replace('?','')

        if len(word) > 3:
            result.append(word)
    return(result)
    pass

print(q5('Hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'))
'''
#Question 6
#Harley's Solution [Same As My Solution]
'''
def q6(sentence):
    words = sentence.split()
    count = {}
    maxCount = 0
    maxWord = None

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            if count[word] > maxCount:
                maxWord = word
                maxCount = count[word]

    return maxWord
    pass

print(q6('a bike jumped a down the a down down down down down')
'''
#Question 7
#Harley's Solution [Same As My Solution]
'''
def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1 : -1])

print(q7('racecar'))
'''
#Question 8
#Harley's Solution [Same As My Solution]
'''
def q8(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False

    return True
    pass

print(q8([[5,6,7,2],[9,8,4,22]]))
'''
#Question 9
#Harley's Solution [Same As My Solution]
'''
def q9(s,insertionletter):
    try :
        if len(insertionletter) != 1:
            return None

        result = ''
        for letter in s:
            result += letter + insertionletter

        return result
    except TypeError:
        return None

print(q9('test','xy'))
'''
#Question 10
#Harley's Solution [Same As My Solution]
'''
def q10(pointlist):
    (minX, minY) = pointlist[0]
    (maxX, maxY) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y) = pointlist[i]

        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    return [(minX,minY),(maxX,maxY)]
    pass

print(q10([(5,6),(7,2),(3,5)]))
'''


#Memory Test Attempt 1
        #
        #
        #
        #
        #
'''
def q1(a,b,c,epsilon):
    minNum = min(a,b,c)
    maxNum = max(a,b,c)

    if maxNum - minNum <= epsilon:
        return True
    else:
        return False

print(q1(5,6,7,2))
'''

'''
def q2(n):
    minNum = n
    maxNum = 3 * n
    numSum = 0

    while maxNum >= minNum:
        if maxNum % 2 == 1:
            numSum += maxNum
        maxNum -= 1

    return numSum

print(q2(4))
'''

'''
def q3(x,epsilon):
    guess = x / 2

    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess

print(q3(4,0.1))
'''

'''
def q4(s):
    finalstring = ''

    for i in range(len(s)):
        finalstring += i * s[i]

    return finalstring

print(q4('dog'))
'''

'''
def q5(sentence):
    words = sentence.split()

    result = []

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if len(word) > 3:
            result.append(word)

    return result

print(q5('hey diddle diddle the cat and the fiddle, the cow jumped over the moon .'))
'''

'''
def q6(sentence):
    words = sentence.split()
    count = {}
    maxCount = 0
    maxWord = None

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            if count[word] > maxCount:
                maxCount = count[word]
                maxWord = word

    return maxWord
'''

'''
def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])

print(q7('racecar'))
'''

'''
def q8(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False
    return True
    
print(q8([[1,2,3],[4,5,6],[7,8,9]]))
'''

'''
def q9(s,insertionletter):
    try:
        if len(insertionletter) != 1:
            return None

        result = ''

        for letter in s:
            result += letter + insertionletter

        return result

    except TypeError:
        return None

    
print(q9('blue','x'))
'''

'''
def q10(pointlist):
    (minx,miny) = pointlist[0]
    (maxx,maxy) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y) = pointlist[i]

        if x < minx:
            minx = x

        if x > maxx:
            maxx = x

        if y < miny:
            miny = y

        if y > maxy:
            maxy = y

    return [(minx,miny),(maxx,maxy)]


print(q10([(5,6),(7,2),(3,5)]))
'''


#Memory Test Attempt 2
        #
        #
        #
        #
        #
'''
def q1(a,b,c,epsilon):
    maxNum = max(a,b,c)
    minNum = min(a,b,c)

    if maxNum - minNum <= epsilon:
        return True

    return False

print(q1(5,6,7,2))
'''

'''
def q2(n):
    minNum = n
    maxNum = 3 * n

    numSum = 0

    while maxNum >= minNum:
        if maxNum % 2 == 1:
            numSum += maxNum
        maxNum -= 1

    return numSum

print(q2(2))
'''

'''
def q3(x,epsilon):
    guess = x / 2

    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess

print(q3(4,0.1))
'''

'''
def q4(s):

    result = ''
    for i in range(len(s)):
        result += i * s[i]

    return result

print(q4('dog'))
'''

'''
def q5(sentence):
    words = sentence.split()
    result = []

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if len(word) > 3:
            result.append(word)

    return result

print(q5('hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'))
'''

'''
def q6(sentence):
    words = sentence.split()
    count = {}
    maxWord = None
    maxCount = 0

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            if count[word] > maxCount:
                maxCount = count[word]
                maxWord = word

    return maxWord

print(q6('hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'))
'''

'''
def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])

print(q7('racecar'))
'''

'''
def q8(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False

    return True

print(q8([(1,2,3),(4,5,6),(2,8,9)]))
'''

'''
def q9(s, insertionletter):
    try:
        if len(insertionletter) != 1:
            return False

        result = ''
        for letter in s:
            result += letter + insertionletter

        return result

    except TypeError:
        return None

print(q9('blue','x'))
'''

'''
def q10(pointlist):
    (minx,miny) = pointlist[0]
    (maxx,maxy) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y) = pointlist[i]

        if x > maxx:
            maxx = x

        if x < minx:
            minx = x

        if y < miny:
            miny = y

        if y > maxy:
            maxy = y

    return [(minx,miny),(maxx,maxy)]

print(q10([(2,5),(4,7),(6,9)]))
'''


#Memory Test Attempt 3
        #
        #
        #
        #
        #
'''

def q1(a,b,c,epsilon):
    maxNum = max(a,b,c)
    minNum = min(a,b,c)

    if maxNum - minNum <= epsilon:
        return True

    return False


def q2(n):
    minNum = n
    maxNum = 3 * n

    numSum = 0

    while maxNum >= minNum:
        if maxNum % 2 == 1:
            numSum += maxSum

        maxSum -= 1

    return numSum


def q3(x,epsilon):
    guess = x / 2

    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess



def q4(s):
    result = ''

    for i in range(len(s)):
        result += i * s[i]

    return result

def q5(sentence):
    words = sentence.split()
    result = []

    for word in words:
        word.replace
        word.replace
        word.replace
        word.replace

        if len(word) > 3:
            result.append(word)

    return result


def q6(sentence):
    words = sentence.split()
    count = {}
    maxWord = None
    maxCount = 0

    for word in words:
        word.replace
        word.replace
        word.replace
        word.replace

        if word not in count:
            count[word] = 1

        else:
            count[word] += 1
            if count[word] > maxCount:
                maxCount = count[word]
                maxWord = word

    return word


def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])


def q8(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False
    return True

def q9(s,insertionletter):
    try:
        if len(insertionletter) != 1:
            return False

        result = ''

        for letter in s:
            result += letter + insertionletter

        return result

    except TypeError:
        return None


def q10(pointlist):
    (minx,miny) = pointlist[0]
    (maxx,maxy) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y) = pointlist[i]

        if x > maxx:
            maxx = x

        if x < minx:
            minx = x

        if y > maxy:
            maxy = y

        if y < miny:
            miny = y

    return [(minx,miny),(maxx,maxy)]

'''

#Memory practice #4
'''
def q1(a,b,c,epsilon):
    maxNum = max(a,b,c)
    minNum = min(a,b,c)

    if maxNum - minNum <= epsilon:
        return True

    return False

print(q1(5,6,7,2))
'''

'''
def q2(n):
    minNum = n
    maxNum = n * 3

    totalSum = 0

    while maxNum >= minNum:
        if maxNum % 2 == 1:
            totalSum += maxNum
        maxNum -= 1

    return totalSum

print(q2(2))
'''

'''
def q3(x, epsilon):
    guess = x / 2

    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess

print(q3(4,0.1))
'''

'''
def q4(s):
    result = ''

    for i in range(len(s)):
        result += i * s[i]

    return result

print(q4('dog'))
'''

'''
def q5(sentence):
    words = sentence.split()

    result = []

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if len(word) > 3:
            result.append(word)

    return result

print(q5('hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'))
'''

'''
def q6(sentence):
    words = sentence.split()
    count = {}
    maxWord = None
    maxCount = 0

    for word in words:
        word.replace(',','')
        word.replace('.','')
        word.replace('!','')
        word.replace('?','')

        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            if count[word] > maxCount:
                maxCount = count[word]
                maxWord = word

    return maxWord

print(q6('hey diddle diddle the cat and the fiddle, the cow jumped over the moon.'))
'''

'''
def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])

print(q7('racecar'))
'''

'''
def q8(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False

    return True

print(q8([[1,2,3],[4,5,6],[2,8,9]]))
'''

'''
def q9(s,insertionletter):
    try:
        if len(insertionletter) != 1:
            return False

        result = ''

        for letter in s:
            result += letter + insertionletter

        return result

    except TypeError:
        return False

print(q9('blue','x'))
'''

'''
def q10(pointlist):
    (minx,miny) = pointlist[0]
    (maxx,maxy) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y,) = pointlist[i]

        if x < minx:
            minx = x

        if x > maxx:
            maxx = x

        if y < miny:
            miny = y

        if y > maxy:
            maxy = y

    return[(minx,miny),(maxx,maxy)]

print(q10([(2,5),(3,2),(7,4)]))
'''



def q1(a,b,c,epsilon):
    maxnum = max(a,b,c)
    minnum = min(a,b,c)

    if maxnum - minnum <= epsilon:
        return True

    return False

def q2(n):
    minnum = n
    maxnum = n * 3

    numsum = 0

    while maxnum >= minnum:
        if maxnum % 2 == 1:
            numsum += 1
        maxnum -= 1

    return numsum


def q3(x,epsilon):
    guess = x / 2

    while abs(guess ** 2 - x) > epsilon:
        guess = (guess + x / guess) / 2

    return guess


def q4(s):
    result = ''

    for i in range(len(s)):
        result += i * s[i]

    return result


def q5(sentence):
    words = sentence.split()
    result = []

    for word in words:
        word.replace
        word.replace
        word.replace
        word.replace

        if len(word) > 3:
            result.append(word)

    return result


def q6(sentence):
    words = sentence.split()
    count = {}
    maxWord = None
    maxCount = 0

    for word in words:
        word.replace()
        word.replace()
        word.replace()
        word.replace()

        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
            if count[word] > maxCount:
                maxCount = count[word]
                maxWord = word

    return maxWord


def q7(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])


def q8(s,insertionletter):
    try:
        if len(insertionletter) != 1:
            return False

        result = ''

        for letter in s:
            result += letter + insertionletter

        return result

    except TypeError:
        return False


def q9(matrix):
    firstrow = matrix[0]

    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in firstrow:
                return False

    return True


def q10(pointlist):
    (minx,miny) = pointlist[0]
    (maxx,maxy) = pointlist[0]

    for i in range(1,len(pointlist)):
        (x,y) = pointlist[i]

    

















    



