#Syed Yasoob Ali
#500953533
#LAB 8

#Question 1

#from random import *
#
#inRun = False
#L = []
#for j in range(0,20):
#    L.append(randrange(1,7))
#
#for i in range(1,len(L)-1):
#    if inRun == True:
#        if L[i] != L[i-1]:
#            print(')', end = ' ')
#            inRun = False
#    else:
#        if L[i] == L[i+1]:
#            print('(', end = ' ')
#            inRun = True
#    print(L[i], end = ' ')
#    
#if inRun == True:
#    print(')')



#Question 2

#from random import *
#
#inRun = False
#endIndex = 0
#longestValue = 0
#temp = 0 
#L = []
#
#for j in range(0,20):
#    L.append(randrange(1,7))
#
#for i in range(1,len(L)-1):
#    if inRun == True:
#        if L[i] != L[i-1]:
#            if temp > longestValue:
#                longestValue = temp
#                endIndex = i
#            print(')', end = ' ')
#            inRun = False
#            temp = 0
#        else:
#            temp += 1
#    else:
#        if L[i] == L[i+1]:
#            temp += 1
#            print('(', end = ' ')
#            inRun = True
#    print(L[i], end = ' ')
#    
#if inRun == True:
#    print(')')
#
#print()
#L.insert(endIndex - longestValue,'(')
#L.insert(endIndex + 1,')')
#
#print(L)



#QUESTION 3 

#from random import *
#def ReturnIndex():
#   inRun = False
#   endIndex = 0
#   longestValue = 0
#   temp = 0 
#   L = [False, False, True, False, False, False, False, True, True, False, False]
#
#   for i in range(1,len(L)-1):
#       if inRun == True:
#           if L[i]:
#               if temp > longestValue:
#                   longestValue = temp
#                   endIndex = i
#               print(')', end = ' ')
#               inRun = False
#               temp = 0
#           else:
#               temp += 1
#       else:
#           if not L[i]:
#               temp += 1
#               print('(', end = ' ')
#               inRun = True
#       print(L[i], end = ' ')
#    
#   if inRun == True:
#       print(')')
#
#   print()
#   L.insert(endIndex - longestValue,'(')
#   L.insert(endIndex + 1,')')
#
#   print(L)
#   print(endIndex,longestValue)
#   return((endIndex - longestValue),(endIndex + 1))
#print(ReturnIndex())



#Question 4

def occupy(n):

    if n <= 0:
        return('Please input a positive integer greater than 0')

    def Empty(arrayInput):
        
        IndexStart = []
        IndexEnd = []
        lastDifference = 0
        largestIndex = 0

        if  '-' not in arrayInput:
            return(-1,-1)
        
        for index in range(len(arrayInput)):
            if index < len(arrayInput)-1 and arrayInput[index] == arrayInput[index+1]:
                if arrayInput[index]=='-':
                    IndexStart.append(index)

                    while index < len(arrayInput)-1 and arrayInput[index] == arrayInput[index+1]:
                        index += 1
                
                    IndexEnd.append(index)
        
        for index in range(len(IndexStart)):
            if (IndexEnd[index] - IndexStart[index]) > lastDifference:
                lastDifference = IndexEnd[index] - IndexStart[index] + 1
                largestIndex = index
                
        if IndexStart == [] and IndexEnd == []:
            return(0,0)
        
        return(IndexStart[largestIndex],IndexEnd[largestIndex])

    
    L = []
    strOut = ''
    
    [L.append('-') for index in range(n)]
    
    for index in range(len(L)):
        strOut += L[index]
    strOut += '\r\n'
    
    while Empty(L) != (-1,-1):
        if Empty(L) == (0,0):
            for index in range(len(L)):
                if L[index] == '-':
                    L[index] = 'X'
                    break
            
        elif Empty(L) != (0,0):
            L[Empty(L)[0] + round(((Empty(L)[1]) - Empty(L)[0])/2)] = 'X'

        for index in range(len(L)):
            strOut += L[index]
            
        strOut += '\r\n'

    return '\r\n' + strOut

    
print(occupy(9))

#Question 5

#L = [1,2,3,4,1]
#J = []
#for i in range(len(L)):
#    J.append(L[i])
#
#L.reverse()
#def isPal(L):
#    if J == L:
#        return True
#    else:
#        return False
#
#print(isPal(L))
    



    

        
