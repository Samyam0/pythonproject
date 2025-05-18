import random
secretnumber = random.randint(1,100)
print("welcome to the guessing game")
print(" i have thought a number from 1 -100")
attempt = 0 
max_attempt = 10

while attempt<max_attempt:
    attempt+=1
    user = input(f"\nAttempt {attempt}/{max_attempt}. Enter your guess: ")
    try:
      user = int(user)
    except ValueError:
     print("invalid input")
     continue


    if user <secretnumber:
        print("the number is low")
    elif user >secretnumber:
        print("the number is high")
    else:
        print(f"you have guessed the number in {attempt} number of attempts")
        exit()
print("game over")
print(f"the number was: {secretnumber}")


