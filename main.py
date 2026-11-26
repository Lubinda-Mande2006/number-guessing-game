import random

def main():
    while True:
        random_number = random.randint(1,10)
        try:
            user_input = input("Enter a random number between 1 and 10: ")
            number = int(user_input)

            # check if the generated number matches the user input
            if random_number == number:
                print("Great! you've correctly guessed the number")
            elif number == 42:
                print("You guessed secret to life")
            else:
                print("Try again!") 
        except Exception:
            print("Enter a valid number")

        except KeyboardInterrupt:
            print("Goodbye!")
            break
main()                
