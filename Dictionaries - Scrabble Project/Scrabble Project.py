letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points *= 2

# Build your Point Dictionary(1-2)

# checkpoint 1
letter_to_points = {key: value for key, value in zip(letters, points)} 

# checkpoint 2
letter_to_points[" "] = 0
print(letter_to_points)

#returns: {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}

# Score a Word(3-8)

# checkpoint 3-6
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)     
  return point_total

# checkpoint 7
brownie_points = score_word("BROWNIE")

# checkpoint 8
print(brownie_points)
# returns: 15

# Score a Game(9-14)

# checkpoint 9
player_to_words = {"player1": ["BLUE", "TENNIES", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# checkpoint 10
player_to_points = {}

# checkpoint 11-13
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# checkpoint 14
print(player_to_points)
# returns: {'player1': 30, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# Ideas for Further Practice!

# checkpoint 15a
def play_word(player, word):
#this function takes in a player and a word, and adds that word to the list of words they've played
  player_to_words[player].append(word)
 
play_word("player1", "PYTHON")

print(player_to_words)
# returns: {'player1': ['BLUE', 'TENNIES', 'EXIT', 'PYTHON'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# checkpoint 15b - update_point_totals() — turn your nested loops into a function that you can call any time a word is played

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
      
update_point_totals()
print(player_to_points)

# returns: {'player1': 47, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

# checkpoint 15c - make your letter_to_points dictionary able to handle lowercase inputs as well (included above)

# letters += [letter.lower() for letter in letters]
# points *= 2