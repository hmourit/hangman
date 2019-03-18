# Hangman

This is a basic Python implementation of the game of Hangman.

To play, you can clone this repository and install doing the following:

```bash
git clone https://github.com/hmourit/hangman.
cd hangman
pip install .
```

You can use the `HangmanGame` and `Leaderboard` classes by importing the 
package `hangman`. It also provides a CLI that you can launch with the command
`hangman` once the Python package is install. The usage instructions are the following:
```
usage: hangman [-h] [-l LEADERBOARD_PATH] [-d]

Hangman game.

optional arguments:
  -h, --help            show this help message and exit
  -l LEADERBOARD_PATH, --leaderboard LEADERBOARD_PATH
                        Path to a leaderboard file to load/save player scores.
  -d, --debug           Activates debug mode.
```
