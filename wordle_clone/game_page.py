from flask import (
    Blueprint, flash, redirect, render_template,request, session
)

bp = Blueprint('game', __name__)

guess_list:list[str] = []

@bp.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


@bp.route('/guess', methods=['POST'])
def guess():
    guess = None
    if request.method == 'POST':
        guess = request.form['guess']
        session['guessed_words'].append(guess)
        error = None
        
        flash(error)

    return redirect('/')

@bp.route('/',methods=['GET'])
def wordle_game():
    game_board = calculate_game_board(session['guessed_words'])
    guess = "No Guesses Yet"
    if len(session['guessed_words']):
        guess = session['guessed_words'][-1]

    if guess == session['solution_word']:
        return render_template('win.html',guess=guess,game_board=game_board)

    if len(session['guessed_words']) == 6:
        return render_template('loose.html',guess=guess,game_board=game_board)

    return render_template('base.html',guess=guess,game_board=game_board)


def calculate_game_board(guess_list:list[str]) -> list[list[str]]:
    guesses:list[str] = ["_"*5]*6
    hints:list[str] = ["_"*5]*6

    for i, guess in enumerate(guess_list):
        guesses[i] = guess
        hints[i] = get_hint(guess)

    game_board:list[list[str]] = [guesses, hints]

    return game_board

def get_hint(guess:str) -> str:
    hint_list:list[str] = []
    for i, letter in enumerate(guess):
        if letter == session['solution_word'][i]:
            hint_list.append('O')
            continue
        if letter in session['solution_word']:
            hint_list.append('Y')
            continue
        hint_list.append('X')
    hint:str = ''.join(hint_list)
    return hint