import random



def main():
    print("WELCOME TO THE GUESSING GAME")
    print("1. Single Round")
    print("2. Three Rounds")
    print("3. Quit")
    menuInput = int(input("input a number to choose game mode or input 3 to leave"))
    if(menuInput == 1):
        play_single_round()
    elif(menuInput == 2):
        play_three_rounds()
    elif(menuInput == 3):
        print("thanks for playing")
    else:
        print("invalid input")

def play_single_round():
    dealerNum = random.randint(0,100)
    attempts = 0
    maxAttempts = 10
    playerNum = 0

    while(attempts <= maxAttempts):
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
            print('the number was ',dealerNum,' you guessed correctly. CONGRATS!')
            print("it took you", attempts, "guesses to get the correct answer")
            main()
    print("you used all of your attempts! Game over!")
    main()
    
def play_three_rounds():
        roundsWon = 0
        totalScore = 0
        for x in range(3):
            dealerNum = random.randint(0,100)
            attempts = 0
            maxAttempts = 10
            playerNum = 0
            round = 1
            print("game: ", round)
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
                    print("You guessed the number!")
                    attempts == maxAttempts
            roundsWon =+ 1
            totalScore =+ attempts
            round =+ 1
        print("Congratulations! You won", roundsWon, " rounds!")
        print("Your total score is: ", totalScore)
        main()

if __name__ == '__main__':
    main()