def guess_game(NumberOfGuess):
    """
    This function generate a random number between the lower range and upper range as selected by the user
   and check if it tallys with the user guess.

    INPUT: num - (int) number of trials to be allowed

    OUTPUT: (str) message saying whether the user guess is correct or not.
    """

    import random

    print("Welcome to the Guess Game!!!")
    
    min_range = int(input(f'Enter the lower range\n'))
    max_range =  int(input(f'Enter the upper range\n'))
    rand_num = random.randint(min_range,max_range)
    count = 0
    
    while NumberOfGuess != 0 :
        count += 1
        user_guess = int(input('Guess a number between {} and {}\n'.format(min_range,max_range)))

        if user_guess == rand_num:
            NumberOfGuess -= 1
            print("Congratulations!!!, you guessed correctly in {} attempt(s)\n".format(count))
            break
        
        elif user_guess > rand_num:
                NumberOfGuess -= 1
                print("Oops! Your guess is greater than the number, guess a lower number")
                print("You have {} attempts remaining\n".format(NumberOfGuess))
                
        elif user_guess < rand_num:
            NumberOfGuess -= 1
            print("Oops! Your guess is less than the number, guess a higher number")
            print("You have {} attempts remaining\n".format(NumberOfGuess))
            
        if NumberOfGuess == 0:
            print("Sorry you have exhausted your number of trials")
            
   
        
    
