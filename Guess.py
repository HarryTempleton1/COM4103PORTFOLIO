import random



def play_single_round():
    dealerNum = random.randint(0,100)
    attempts = 0
    maxAttempts = 10
    playerNum = 0

    while(attempts < maxAttempts):
        playerNum = int(input('Input a number 0-100'))
        if(playerNum > dealerNum):
            print('The number is lower than your number')
            attempts += 1
            print("you have", 10 - attempts, "attempts left")
        elif(playerNum < dealerNum):
            print('The number is higher than your number')
            attempts += 1
            print("you have", 10 - attempts, "attempts left")
        elif(playerNum == dealerNum):
            win(dealerNum, attempts)
    print("you used all of your attempts! Game over!")
    
    
    

def win(dealerNum, attempts):
    
    print('the number was ',dealerNum,' you guessed correctly. CONGRATS!')
    print("it took you", attempts, "guesses to get the correct answer")

play_single_round()