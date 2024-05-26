import functools
from flask import (
    Blueprint, flash, g, redirect, render_template,request, session, url_for
)

bp = Blueprint('game', __name__)

guess_list:list[str] = []

@bp.route('/',methods=('GET','POST'))
def wordle_game():
    guess = None
    if request.method == 'POST':
        guess = request.form['guess']
        error = None
        guess_list.append(guess)
        
        if not guess:
            error = 'Please enter a guess.'
    
        flash(error)

    return render_template('base.html',guess=guess,guess_list=guess_list)