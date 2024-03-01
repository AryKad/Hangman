from hangman_Art import stages
from hangman_words import word_list
print( ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
import random
chosen_word = random.choice(word_list)
display = ""
answer_list = []
for i in range(len(chosen_word)):
  display += "_"
  answer_list +="_"
print(f"Given word : {display}")
game_over = False
lives = 7
while game_over != True:
  guess = input("Guess a letter: ").lower()
  count = 0
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      answer_list[i] = chosen_word[i]
      count +=1
  print(answer_list)
  if "_" not in answer_list:
    print("You win.")
    game_over = True
  elif count == 0 :
    print(stages.pop(-1))
    lives -=1
    count+=1
    if lives == 0:
      print("You lose.")
      print(f"The word was {chosen_word}")
      game_over = True