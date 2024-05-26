## Game Loop
# Game selects a Solution word
# Player supplies their guess => input
# Game gives hints based onthe guess
#   Wich letters are in the correct location
#   Which are in the solution but not correct location

def get_player_input() -> str:
    invalid_guess = True
    while invalid_guess:
        guess = input()
        if len(guess) != 5 or not guess.isalpha():
            invalid_guess = True
            print("This is not a valid guess, guess again.")
        else:
            invalid_guess = False

    return guess

def check_if_solved(solution:str, guess:str) -> bool:
    continue_game_loop = True
    hint = ['n','n','n','n','n']
    if solution == guess:

        print(' '.join(['G']*5))
        print("You got the answer!")
        return not continue_game_loop
    for i, letter in enumerate(guess):
        if letter == solution[i]:
            hint[i] = 'G'
        if letter in solution:
            hint[i] = 'Y'
    print(' '.join(hint))
    return continue_game_loop

def wordle_game():
    solution = "idols"
    guesses = [None,None,None,None,None,None]
    n_guesses = 0
    game_loop = True
    
    while game_loop:
        for i in range(6):
            if guesses[i] is not None:
                print(' '.join(list(guesses[i])))
            else:
                print("_ _ _ _ _")
        print("Type your next guess:")
        guess = get_player_input()
        game_loop = check_if_solved(solution, guess)
        print("\n")
        guesses[n_guesses] = guess
        n_guesses += 1
    
        if n_guesses > 5:
            game_loop = False

    for i in range(6):
            if guesses[i] is not None:
                print(' '.join(list(guesses[i])))
            else:
                print("_ _ _ _ _")

if __name__ == "__main__":
    wordle_game()
