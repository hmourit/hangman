import argparse
import os

from hangman.core import HangmanGame
from hangman.core import Leaderboard


def main():
    """CLI interface for the Hangman Game."""
    args = get_args()
    leaderboard_path = args.leaderboard_path
    debug = args.debug

    print('\n\nWelcome to the Hangman game.\n\n')

    if leaderboard_path is not None and os.path.isfile(leaderboard_path):
        leaderboard = Leaderboard.from_file(leaderboard_path)
    else:
        leaderboard = Leaderboard()

    name = input("What's your name? ").strip()
    if name in leaderboard:
        print(f'Your previous score is {leaderboard.get_player_score(name)}. '
              f'Try to improve it!')

    print("Let's start a new game.")

    game = HangmanGame()
    if debug:
        print(f'DEBUG: The chosen word is: {game.current_word}')

    while not game.is_finished:
        print(game.state_str())

        action = None
        while action not in {'', 'L', 'l', 'g', 'G'}:
            action = input('Do you want a new letter [L] or try to guess the word [g]?')
            if debug:
                print(f'DEBUG: action=<{action}>')

        if action in {'', 'L', 'l'}:
            letter = input('What letter do you want: ')
            letter = letter.lower()

            if game.check_letter(letter):
                print('Your letter is in the word.')
            else:
                print(f'Your letter is not in the word.')

        elif action in {'g', 'G'}:
            guess = input('What is your guess of the word? ')
            if game.check_word(guess.lower()):
                print('You guessed it.')
            else:
                print(f'{guess.lower()} is not the word. Keep trying.')

    if game.won:
        print(f'Congratulations! You won! Score: {game.score()}')
    else:
        print('Sorry, you lost!')

    if game.won:
        if name in leaderboard and game.score() > leaderboard.get_player_score(name):
            print(f'You improved your best score.')

        print('Updating leaderboard...')
        leaderboard.update_player_score(name, game.score())

        if leaderboard_path is not None:
            leaderboard.to_file(leaderboard_path)

        print('The top 5 players are:')
        for player, score in leaderboard.top_n_players(5):
            print(f'{player} --- {score}')


def get_args():
    parser = argparse.ArgumentParser(description='Hangman game.')
    parser.add_argument('-l', '--leaderboard', dest='leaderboard_path', required=False,
                        help='Path to a leaderboard file to load/save player scores.')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Activates debug mode.')
    args = parser.parse_args()
    return args
