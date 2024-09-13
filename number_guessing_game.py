import time
import random

def play_again():
    play_again_ask = input("Do you want to play again?(Y/N)")
    play_again_ask_upper = play_again_ask.upper()
    if(play_again_ask_upper == "Y"):
        game()
    else:
        sad_to_go()

def win():
    print("WELL DONE! you win")
    play_again()


def lost():
    print("Sorry you lost:(")
    play_again()
    

def sad_to_go():
    print("Sad to see you go :( See you later.")
    time.sleep(2)
    quit()

def game():
    
    print("Welcome to Number Guessing game!")
    difficulty = input("Please select the difficulty: \n A.Easy(0-10) \n B.Medium(0-50) \n C.Hard(0-100) \n D.Very Hard(0-1000)")
    difficulty_upper = difficulty.upper()
    if(difficulty_upper == "A"):
        random_number = random.randint(0,10)
        hearts=3
        while True:
            if(hearts==0):
                lost()
            player_guess = input("Please guess the number : ")
            player_guess_int = int(player_guess)
            if(player_guess_int==random_number):
                win()
            if(player_guess_int>random_number):
                print("Lower!")
                hearts-=1
            if(player_guess_int<random_number):
                print("Higher!")
                hearts-=1
    elif(difficulty_upper=="B"):
        random_number = random.randint(0,50)
        hearts=5
        while True:
            if(hearts==0):
                lost()
            player_guess = input("Please guess the number : ")
            player_guess_int = int(player_guess)
            if(player_guess_int==random_number):
                win()
            if(player_guess_int>random_number):
                print("Lower!")
                hearts-=1
            if(player_guess_int<random_number):
                print("Higher!")
                hearts-=1
    elif(difficulty_upper=="C"):
        random_number = random.randint(0,100)
        hearts=7
        while True:
            if(hearts==0):
                lost()
            player_guess = input("Please guess the number : ")
            player_guess_int = int(player_guess)
            if(player_guess_int==random_number):
                win()
            if(player_guess_int>random_number):
                print("Lower!")
                hearts-=1
            if(player_guess_int<random_number):
                print("Higher!")
                hearts-=1
    elif(difficulty_upper=="D"):
        random_number = random.randint(0,1000)
        hearts=10
        while True:
            if(hearts==0):
                lost()
            player_guess = input("Please guess the number : ")
            player_guess_int = int(player_guess)
            if(player_guess_int==random_number):
                win()
            if(player_guess_int>random_number):
                print("Lower!")
                hearts-=1
            if(player_guess_int<random_number):
                print("Higher!")
                hearts-=1
    else:
        sad_to_go()

            
            



def main():
    want_play = input("Do you want to play?(Y/N)")
    want_play_upper = want_play.upper()
    if(want_play_upper == "Y"):
        game()
    else:
        sad_to_go()

if __name__ == "__main__":
    main()