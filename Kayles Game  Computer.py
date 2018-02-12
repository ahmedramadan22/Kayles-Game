print("                      Welcom To Kayles Game ")
game=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
size=20
print(game)
import random
y=random.randint(1,2)
if y==1:
    while (True):
        check=0
        complete1=True
        game[9]=0
        game[10]= 0
        print("Computer: ",game)
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
        for k in range(0,20,1) :
            if (game[k] != 0):
                check+=1
        if (check == 0):
            print ("Player 1 Wins ")
            break
        check=0
        complete1 = True
        pc=20-p1
        while (complete1) :
            while (True):
                if (p1n == 1 ):
                    game[pc]=0
                    complete1 = False
                    break
                elif (p1n == 2):
                    game[pc]=0
                    game[pc-1]=0
                    complete1 = False
                    break
                        
        for k in range (0,20,1) :
            if (game[k] != 0):
                check+=1
        if (check == 0):
            print ("Computer Wins ")
            break
            
if y==2:
    while(True):
        check=0
        complete1=True
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
                    else:
                        print ("Error\n")
                        break     
            
        print (game)
        for k in range(0,20,1) :
            if (game[k] != 0):
                check+=1
        if (check == 0):
            print ("Player 1 Wins ")
            break
        check = 0
        complete1 = True
        while (complete1) :
            while(True):
                p1n=random.randint(1,2)
                break
            while(True):
                if (p1n == 1 ):
                    p1=random.randint(1,20)
                    if (game[p1-1] == 0):
                        break
                    else:
                        game[p1-1]=0
                        complete1 = False
                        break
                elif(p1n == 2 ):
                    p1=random.randint(1,20)
                    if (game[p1-1]!=0 and game[p1]!=0 ):
                        game[p1-1]=0
                        game[p1] = 0
                        complete1 = False
                        break
                    else:
                        break
        print("Computer: ",game)                 
        for v in range (0,size) :
            if (game[v] != 0):
                check+=1
        if (check == 0):
            print ("Computer Wins ")
            break
                
                        
                    
                        
                    
                
                
            
        
                
                
            
    
    
    
        
                    
                
                
                
                
                
            

    
    
                
                
                
            
            
        
            
