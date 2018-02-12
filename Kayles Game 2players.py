print("                      Welcom To Kayles Game ")
from random import *
game = []

size = randint(5,30)
print ("Size : " , size)
for i in range (1,size+1):
    game.append(i)
print (game)

print (" Game Rules \n 1/Please Choose 1 Number or 2 Numbers Beside Each Others \n 2/zero Is Exclusive \n 3/No Letters Accepted")
while (True):
    check = 0
    complete1 = True
    while (complete1) :
        while (True):
            p1n = int (input ("Player 1 Number of Tokens : "))
            if (p1n == 1 or p1n == 2 ) :
                break
            else:
                print ("Error")
                
        while (True):
            if (p1n == 1 ):
                p1 = int (input ("Enter Your Tokens Number : "))
                if (p1>size ):
                    print ("Error")
                    break
                elif (game[p1-1] == 0 or p1 <=0):
                    print ("Error .. Try Again")
                    break
                
                else :
                    game[p1-1]=0
                    complete1 = False
                    break
            elif (p1n == 2 ):
                p1 = int (input("Enter Your 2 Tokens Numbers : "))
                if p1 >= size :
                    print ("Error")
                    break
                elif (game[p1-1]!=0 and game[p1]!=0):
                        game[p1-1]=0
                        game[p1] = 0
                        complete1 = False
                        break
                else :
                    print ("Error\n")
                    break
    print (game)                    
    for k in range (0,size) :
        if (game[k] != 0):
            check+=1
    if (check == 0):
        print ("Player 1 Wins ")
        break
    check = 0
    complete1 = True
    while (complete1) :
        while (True):
            p1n = int (input ("Player 2 Number of Tokens : "))
            if (p1n == 1 or p1n == 2 ) :
                break
            else:
                print ("Error")
                
        while (True):
            if (p1n == 1 ):
                p1 = int (input ("Enter Your Tokens Number : "))
                if (p1>size):
                    print ("Error")
                    break
                elif (game[p1-1] == 0 or p1 <=0):
                    print ("Error .. Try Again")
                    break
                else :
                    game[p1-1]=0
                    complete1 = False
                    break
            elif (p1n == 2 ):
                p1 = int (input("Enter Your 2 Tokens Numbers : "))
                if (p1>=size):
                    print ("Error")
                    break
                    
                elif (game[p1-1]!=0 and game[p1]!=0 ):
                        game[p1-1]=0
                        game[p1] = 0
                        complete1 = False
                        break
                else :
                    print ("Error\n")
                    break        
                        
    print (game)                    
                    
    for v in range (0,size) :
        if (game[v] != 0):
            check+=1
    if (check == 0):
        print ("Player 2 Wins ")
        break
    
    
    
        
                    
                
                
                
                
                
            
