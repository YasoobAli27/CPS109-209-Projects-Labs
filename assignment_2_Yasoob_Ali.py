#Syed Yasoob Ali
#500953533
#2019.11.25
#Assignment 2


def crossword(L):

    #creates an empty board

    blank = ' '
    number = 20
    
    board = [[ blank ] * number for i in range(number)]
    
    largest = 0
    largestindex = 0
    
    #cycles through the list in order to find the largest string
    for k in range(len(L)):
        if len(L[k]) > largest:
            largest = len(L[k])
            largestindex = k
            
    #Adds first string to the board
    def addWord(board, string):
        if len(string) > len(board):
            return False
        xi = round((len(board)-len(string))/2)
        yi = round((len(board)-1)/2)
        for x in range(len(string)):
            board[yi][xi+x] = string[x]            
        return board

    #calls the addWord function to insert the first string directly in the middle
    addWord(board, L[largestindex])
    
    L.pop(largestindex)
    L.sort(key = len, reverse = True)    
    lengthAvg = 0
    
    sum = 0
    
    for y in range(len(L)):
        sum += len(L[y])
        lengthAvg = round(sum/len(L))

    #will check to see if the string will fit inside the crossword
    conditionMet = False
    #Adds all words that can't be added to crossword into this list
    badWords = []

    #Vertical function takes in 2 inputs: the board and a string from the string list
    #Will check to see if the string can be added vertically or not
    def vertical(board, string):        
        def verticalWorks(board, string, row, col):
            if len(string) > len(board[row]):
                return False
            index = 0
            indexy = -1
            
            if board[row][col] in string:
                igrid=0
                indexy = string.find(board[row][col])
                
                for index in range(len(string)):
                    igrid = ((row+index)) - indexy                   
                    if igrid >= len(board[row]) or igrid < 0:
                        return(False, '', -1)
                    if board[igrid][col] != string[indexy] and board[igrid][col] != ' ':
                        if board[igrid][col] not in string:
                            return(False, '', -1,(igrid, col))
                    
                    if board[igrid][col + 1] != ' ':
                        if col < len(board[row])-1:
                            if board[igrid][col] != string[indexy]:
                                return(False, '', -1,(igrid, col))
                    
                    if col > 0 and board[igrid][col - 1] != ' ':
                        if board[igrid][col] != string[indexy]:
                            return(False, '', -1,(igrid, col))                    
                    
                stringnew = ''    
                for index in range(len(string)):
                    igrid = ((row+index)) - indexy
                    stringnew += board[igrid][col]
                    
                if string in stringnew:
                    return(False, '', -1)
                
                return (True, string[string.find(board[row][col])],  string.find(board[row][col]), (row, col), igrid)
            return(False, '', -1)
        
        verticalCondition = None
        for row in range(len(board)):
            for col in range(len(board[row])):
                verticalCondition = verticalWorks(board, string, row, col)
                
                if verticalCondition[0]: 
                    for index in range(len(string)):
                        nextindex = ((verticalCondition[4]-(len(string)-1)) + index)
                        if nextindex >= len(board[row]) or nextindex <= 0:
                            return False
                        board[nextindex][verticalCondition[3][1]] = string[index]                       
                    return True
        return False


    
    #Horizontal function will take in 2 inputs as well, similar to vertical
    #Will return True or False
    def horizontal(board, string):
        def horizontalWorks(board, string, row, col):
            if len(string) > len(board[row]):
                return False
            
            indexX = -1
            
            if board[row][col] in string:
                indexX = string.find(board[row][col])
                igrid = 0
                
                for index in range((len(string)-indexX)-1):
                    igrid = (col+index) + 1
                    
                    if igrid >= len(board[col]) or igrid < 0:
                        return(False, '', -1)
                    
                    if board[row][igrid] != string[indexX]:
                        if board[row][igrid] != ' ':
                            return(False, '', -1,(row, igrid))
                    
                    if board[row + 1][igrid] != ' ':
                        if row < len(board)-1:
                            if board[row][igrid] != string[indexX]:
                                return(False, '', -1,(igrid, col))
                    
                    if board[row][igrid] != string[indexX] and board[row - 1][igrid] != ' ' and board[row][igrid] not in string:
                        if row > 0:
                            return(False, '', -1,(igrid, col))
                    
                stringnew = ''    
                for index in range((len(string)-indexX) - 1):
                    igrid = (col+index) + 1
                    stringnew = stringnew + board[row][igrid]
                    
                if string in stringnew:
                    return(False, '', -1)                
                return (True, string[string.find(board[row][col])],  string.find(board[row][col]), (row, col), igrid)
            return(False, '', -1)
        
        horizontalCondition = None
        for row in range(len(board)):
            for col in range(len(board[row])):
                horizontalCondition = horizontalWorks(board, string, row, col)
                
                if horizontalCondition[0]:
                    for index in range(len(string)):
                        nextindex = ((horizontalCondition[4]-(len(string)-1)) + index)

                        if nextindex <= 0 or nextindex >= len(board[row]):
                            return False

                        board[horizontalCondition[3][0]][nextindex] = string[index]                      

                    return True
        return False
            

    #Finally, before we print the board, we must run 2 for loops to append the bad
    #words into the badwords list
    for j in range(len(L)):
        if len(L[j]) >= lengthAvg:
            conditionMet = vertical(board, L[j])
            if conditionMet == False:
                badWords.append('v' + str(j))
        else:
            conditionMet = horizontal(boardn, L[j])
            if conditionMet == False:
                badWords.append('h' + str(j))

      
    for k in range(len(badWords)):
        if 'v' in badWords[k]:
            conditionMet = horizontal(board, L[int(badWords[k][1::1])])
            if not conditionMet:
                badWords[k] = 'h' + str(k)
                
            if conditionMet:
                badWords[k] = 'F'
                
        elif 'h' in badWords[k]:
            conditionMet = vertical(board, L[int(badWords[k][1::1])])
            if not conditionMet:
                badWords[k] = 'v' + str(k) 
            if conditionMet:
                badWords[k] = 'F'


    def createboard(board):
        c = board.copy()
        string1 =''    
        for x in range(len(c)):         
            for y in range(len(c[x])):
                string1 += c[x][y]
            string1 += '\r\n'        
        return string1
                          
                
    print(createboard(board)) 

L1 = ['zzz', 'apple', 'leg', 'grand', 'destroy','energy']

L2 = ['test', 'tree', 'edmonton']

crossword(L1)
crossword(L2)

