import heapq
import random

WORDS = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']
MAX_MISSES = 5


class HangmanGame:
    """Holds the state of a game of Hangman."""
    def __init__(self, vocabulary=WORDS, max_misses=MAX_MISSES):
        self.VOCABULARY = vocabulary
        self.MAX_MISSES = max_misses
        self.current_word = self._get_word()
        self.guessed_letters = set()
        self.n_misses = 0
        self.guess_trials = 0
        self.is_finished = False
        self.won = None

    def _get_word(self):
        """Selects a random word from the vocabulary."""
        return random.choice(self.VOCABULARY)

    def state_str(self):
        """Returns a string representation of the current state."""
        return ' '.join(l if l in self.guessed_letters else '_' for l in self.current_word)

    def score(self):
        """Computes the score."""
        return 100 - (self.guess_trials + len(self.guessed_letters) + self.n_misses)

    def check_letter(self, letter):
        """Checks whether a letter is present in the word and updates game state."""
        if self.is_finished:
            raise ValueError("You can't check more letters, you've reached the limit.")
        if letter in self.current_word:
            self.guessed_letters.add(letter)
            if set(self.current_word) == self.guessed_letters:
                self.is_finished = True
                self.won = True
            return True
        else:
            self.n_misses += 1
            if self.n_misses >= self.MAX_MISSES:
                self.is_finished = True
                self.won = False
            return False

    def check_word(self, word):
        """Checks whether a given word is correct and updates game state."""
        if self.is_finished:
            raise ValueError("You can't try to guess the word, the game is already finished.")
        if word == self.current_word:
            self.is_finished = True
            self.won = True
            return True
        else:
            self.guess_trials += 1
            return False


class Leaderboard:
    """Holds a leaderboard of players and their scores."""
    def __init__(self, scores=None):
        self.scores = scores or {}

    def __contains__(self, item):
        return item in self.scores

    def update_player_score(self, player, score):
        """Updates score for player if higher than the previous."""
        self.scores[player] = max(self.scores[player] if player in self.scores else 0, score)

    def get_player_score(self, player):
        """Returns score of a player."""
        return self.scores.get(player, None)

    def top_n_players(self, n):
        """Returns top n pairs of (player, score) according to the score."""
        return heapq.nlargest(n, self.scores.items(), key=lambda kv: kv[1])

    @classmethod
    def from_file(cls, path):
        """Creates a Leaderboard from a file with one 'player,score' record per line."""
        scores = {}
        with open(path, 'r') as f:
            for line in f:
                print(line)
                if line == '':
                    continue
                try:
                    player, score = line.split(',')
                    score = int(score)
                except ValueError:
                    print('Each line should have the format "player_name,score".')
                    raise ValueError('Incorrect file format.')

                scores[player] = score

        return Leaderboard(scores)

    def to_file(self, path):
        """Saves Leaderboard to a file."""
        with open(path, 'w') as f:
            f.writelines(f'{player},{score}\n' for player, score in self.scores.items())
