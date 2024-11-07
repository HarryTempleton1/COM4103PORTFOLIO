#This library allows me to create a random number for the player to guess
import random

def main():
    print("WELCOME TO THE GUESSING GAME")
    print("1. Single Round")
    print("2. Three Rounds")
    print("3. Quit")
    menuInput = int(input("input a number to choose game mode or input 3 to leave"))
    #sends the flow of code to the function for the game mode chosen
    if(menuInput == 1):
        play_single_round()
    elif(menuInput == 2):
        play_three_rounds()
    elif(menuInput == 3):
        print("thanks for playing")
    else:
        print("invalid input")

def play_single_round():
    #chooses a random number between 0 and 100
    dealerNum = random.randint(0,100)
    attempts = 0
    maxAttempts = 9
    playerNum = 0
    #while loop that checks if the player has reached the max amount of attempts
    while(attempts < maxAttempts):
        playerNum = int(input('Input a number 0-100'))
        #if statement to tell the user if their guess was higher lower or correct
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
    #if the number of attempts becomes greater than the maximum attempts a message saying you loose with be printed and you will be sent back to the main menu
    print("you used all of your attempts! Game over!")
    main()
    
def play_three_rounds():
        #variables to keep track of the amount of rounds won and the users total amount of guesses or score
        roundsWon = 0
        totalScore = 0
        round = 0
        #a for loop to run the game 3 times
        for x in range(3):
            dealerNum = random.randint(0,100)
            attempts = 0
            maxAttempts = 9
            playerNum = 0
            round += 1
            print("game: ", round)
            
            while(attempts <= maxAttempts):
                playerNum = int(input('Input a number 0-100'))
                if(playerNum > dealerNum):
                    print('The number is lower than your number')
                    attempts += 1
                    print("you have", 10 - attempts, "attempts left")
                if(playerNum < dealerNum):
                    print('The number is higher than your number')
                    attempts += 1
                    print("you have", 10 - attempts, "attempts left")
                if(playerNum == dealerNum):
                    print("You guessed the number!")
                    #adds the amount of guesses and rounds won to your score
                    roundsWon += 1
                    totalScore += attempts
                    #breaks the while loop and allows the next game to start
                    break
        print("Congratulations! You won", roundsWon, " rounds!")
        print("Your total score is: ", totalScore)
        main()
#loads main menu
if __name__ == '__main__':
    main()