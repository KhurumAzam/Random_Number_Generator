import random

def main():
    print("Welcome to the random number generator \n")
    computer_number = int(user_difficulty())
    user_number = int(user_input())
    while user_number != computer_number:
      if user_number > computer_number:
        print("That's the incorrect number. It's greater than what you've inputted")
      else:
        print("That's the incorrect number. It's less than what you've inputted")
      user_number = int(user_input())
    print("You Win!!! The number was " + str(computer_number))

def user_difficulty():
    user_input=0
    while int(user_input) < 1 or int(user_input) > 4:
        print("Pick a difficulty:")
        print("1. Easy (1-100)")
        print("2. Medium (1-500)")
        print("3. Hard (1-1000")
        print("4. Insane (1-2000)")
        user_input=input()
        if (user_input.isnumeric() == False):
            print("Pick a valid option from menu")
            user_input = 0
        elif (user_input.isnumeric() == True):
            if(int(user_input) < 1 or int(user_input) > 4):
                print("Pick a valid option from menu")
                user_input=0
        else:
            print("Programmer has an error and needs a coffee break :(")
            quit()
    return user_input

def user_input():
    print("Pick a number: ")
    number = input()
    while number.isnumeric() == False:
        print("This is invalid input (ex. fraction, letter, etc.), please pick a number: ")
        number = input()
    return number

def computer_input(difficulty):
    if difficulty == 1:
        return random.randint(1, 100)
    elif difficulty == 2:
        return random.randint(1, 500)
    elif difficulty == 3:
        return random.randint(1,1000)
    elif difficulty == 4:
        return random.randint(1, 2000)
    else:
        print("Programmer has an error and needs a coffee break :(")
        quit()

if __name__ == "__main__":
    main()
