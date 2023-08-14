import random
import os

print("""                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ \n""")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

list_of_words = [
    "accept", "accuse", "achieve", "address", "advice", "against", "already", "always", "another", "anyone",
    "anything", "anyway", "applied", "arrived", "article", "balance", "become", "believe", "between", "beyond",
    "billion", "business", "careful", "central", "certain", "chance", "clearly", "closely", "company", "compare",
    "complete", "condition", "consider", "continue", "control", "correct", "country", "courage", "daughter", "decide",
    "describe", "design", "develop", "disappear", "discover", "economic", "education", "effect", "encourage", "especially",
    "evidence", "explain", "express", "familiar", "finally", "follow", "foreign", "friendly", "future", "general",
    "government", "happen", "happening", "history", "however", "important", "increase", "indicate", "industry", "instead",
    "interest", "knowledge", "language", "lawyer", "magazine", "maintain", "majority", "manager", "material", "measure",
    "medicine", "mention", "message", "method", "million", "minute", "morning", "necessary", "nothing", "obvious",
    "officer", "official", "operation", "opportunity", "ordinary", "original", "particular", "perfect", "personal", "politics",
    "popular", "position", "possible", "practical", "prepare", "present", "pressure", "probably", "problem", "process",
    "produce", "product", "professor", "property", "protect", "provide", "public", "purpose", "question", "recently",
    "relationship", "religious", "remember", "represent", "research", "scientist", "security", "society", "sometimes",
    "specific", "statement", "strategy", "structure", "success", "suddenly", "suggest", "support", "suppose", "surface",
    "surprise", "system", "television", "therefore", "thousand", "together", "traditional", "usually", "wonderful", "writing"
]

chosen_word = random.choice(list_of_words).lower()
word_length = len(chosen_word)
end_of_game = False
lives = len(stages)


display = []

for _ in range(word_length):
# for _ in chosen_word:
    display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()  

    os.system('clear')

    if guess in display:
        print(f"You've already guessed {guess}")
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if  letter == guess:
              display[position] = letter
      
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess!\n{stages[lives]}")
        if lives == 0:
            print("You lose")
            end_of_game = True
   
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")








