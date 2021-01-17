import random

class game():
  def __init__(self, f, d):
    self.debug = d
    self.file_name = f
    self.word = str(self.random_line_from_file(self.file_name))
    self.guesses = list()

    if self.debug == True:
      print('[DEBUG] ' + str(self) + ' initialized.')
      print('[DEBUG] word set to "{}"'.format(self.word.replace('\n', '')))

  def run(self):
    if self.debug == True:
      print('[DEBUG] Running...')
    
    while True:
      print('(Enter "QUIT" to stop playing)')
      guesses_remaining = (len(self.word) * 2) - len(self.guesses)
      s = (' ' * len(self.guesses)) + 'x' + ('~' * guesses_remaining) + '[BOMB]'
      if guesses_remaining == 0:
        self.lose()
        break
      else:
        print(s)
        
      display_word = ''
      for c in range(len(self.word) - 1):
        if self.word[c] in self.guesses:
          display_word = display_word + self.word[c] 
        else:
          display_word = display_word + '_'
      if display_word.count('_') == 0:
        self.win()
        break 
      print('{}. Guess the word, letter by letter! "{}"'.format(len(self.guesses), display_word))
      guess = input('Your Guess: ')
      if guess != 'QUIT':
        if len(guess) > 0:
          if guess[0] in self.guesses:
              print('You already guessed that.')
          else:
            if guess[0] in self.word:
              print('Good job! {} is in the hidden word!'.format(guess[0]))
            else:
              print('Wrong, unlucky.')
            self.guesses.append(guess[0])
        else:
          pass
      else:
        self.quit()
        break

      if self.debug == True:  
        print(self.guesses)
      print('')

  def win(self):
    print('You win!! Good job')

  def lose(self):
    print('You lost.... The word was "{}".  Better luck next time.'.format(self.word.replace('\n', '')))

  def quit(self):
    print('\nGame stopped. Thanks for playing.')

  def random_line_from_file(self, file_name):
    with open(file_name, 'r') as file:
      l = file.readlines()
      y = random.randint(0, len(l)) - 1
      return l[y] 

myGame = game('words.txt', False)
myGame.run()
