import random as rd

A=int(input('enter the start of range: '))
B=int(input('enter the end of the range: '))
computer=rd.randint(A,B)
counter=0
wrong=0
while True:
    if wrong<3: 
        player=int(input("Guess the Number between range :"))
        if player==00:
            print('Your Score is :',counter)
            print('You ended the game.')
            break
        elif player==computer:
            print('you guessed correct, You get a point collected in your wallet. ')
            counter+=1
            A=int(input('enter the start of range: '))
            B=int(input('enter the end of the range: '))

            computer=rd.randint(A,B)
            wrong*=0
        else:    
            wrong+=1
            if player >computer:
                print('Have one more try ,your guess was high.')

                continue
            else:
                print('Have one more try, Your guess was low.')    
                continue
    else:
        
        print('You have attempted maximum of three times wrong.')   
        print('Your Score till now is :',counter) 
        break    