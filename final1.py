import random
import copy


print("\n WELCOME TO HANGMAN GAME----")
print('''
             _______
            |       |
            |       O
            |      \|/
            |       |
         ___|___   / \ 
                         ''')
print("Let's start the game......")


keywords = {
    'animals': ['lion', 'fox', 'elephant'],
    'fruits': ['apple', 'pineapple', 'watermelon']
}
key, value = random.choice(list(keywords.items()))
j = random.choice(range(0, 2))
print(f"\n The topic of hangman is {key}
")
length_key = len(value[j])
unique = set(value[j])

inputstring = "_" * length_key
input_list = list(inputstring)
iteration=0
lives = 0
while iteration != len(unique):


    if lives == 5:
        print('''
             _______
            |       |
            |       O
            |      \|/
            |       |
         ___|___   / \ 
                         ''')
        break
    
    else:
        word = input("\n Guess the letter: ")
    
    found = 0
    check = 0

    while check < length_key:
      if input_list[check]=="_" :

        if value[j][check] == word:
            input_list[check] = word
            found = found + 1

        else:
            input_list[check] = "_"
      
        check = check + 1

      else:
         check = check + 1
   
    if found == 0:
        print("Opps!! the value is Incorrect")
        new_str = ''.join(input_list)
        print(new_str)  
        lives = lives+1
        if lives == 1:
            print('''
                 _______
                |       |
                |       
                |      
                |       
             ___|___    
                            ''')
            
        elif lives == 2:

            print('''
                 _______
                |       |
                |       O
                |      
                |       
             ___|___    
                            ''')
        
        elif lives == 3:
            print('''
                 _______
                |       |
                |       O
                |      \|/
                |       
             ___|___    
                            ''')
        
        elif lives == 4:
            print('''
                 _______
                |       |
                |       O
                |      \|/
                |       |
             ___|___    
                            ''')

  
    else:
        new_str = ''.join(input_list)
        iteration=iteration + 1
        print(new_str)

print("Game is Over")
