import random
import copy

# def play():
# print(f"\n length of the word is {length_key}")


print("\n WELCOME TO HANGMAN GAME----")
print('''
             _______
            |       |
            |       O
            |      \|/
            |       |
         ___|___   / \
                        ''')

# keywords = {
# 'animals' : [['l','i','o','n'],['f','o','x'],['e','l','e','p','h','a','n','t']] ,
# 'fruits'  : [['a','p','p','l','e'],['p','i','n','e','a','p','p','l','e'],['w','a','t','e','r','m','e','l','o','n']]
#          }

keywords = {
    'animals': ['lion', 'fox', 'elephant'],
    'fruits': ['apple', 'pineapple', 'watermelon']
}
key, value = random.choice(list(keywords.items()))
j = random.choice(range(0, 2))
# search_word=value[i]
print(f"\n The topic of hangman is {key} and {value[j]}")
length_key = len(value[j])
unique = set(value[j])

inputstring = "_" * length_key
input_list = list(inputstring)
print(inputstring)
#iteration = 5 + len(unique)
iteration=0
lives = 0
while iteration != len(unique):
    if lives == 5:
        break
    else:
      # print(f"\n The topic of hangman is {key} and {value[j]}" )
      # length_key = len(search_word)

      # play()

      # word = input("\n Guess the letter: ")
      # inputstring = "_ " * length_key
      # print(inputstring)
        word = input("\n Guess the letter: ")
    # position=(search_word.find(word))

    # if position== -1 :
    #   chance=chance-1
    #   print(f'Incorrect. You have only {chance} lives now')

    # else:
    #    inputstring=inputstring.replace(inputstring[position],search_word[position])
    #   print(f's:{position}')
    # inputstring[position]=search_word[position].copy()
    #    print(inputstring)

    found = 0
    check = 0

    while check < length_key:
      if input_list[check]=="_" :

        if value[j][check] == word:
            input_list[check] = word
            found = found + 1

            # for word in value[j][check] :
            # input_list[check]=word
            # new_str=''.join(input_list)
            # found = found +1

        else:
            input_list[check] = "_"
            # lives=lives+1

        check = check + 1

      else:
         check = check + 1
   
    if found == 0:
        print("Incorrect")
        new_str = ''.join(input_list)
        print(new_str)  
        lives = lives+1
    
    

    else:
        new_str = ''.join(input_list)
        iteration=iteration + 1
        print(new_str)

print("Game completed")
#iteration = iteration-1

# i = 0
# while i < length_key :
#   if value[j][i] == word:
#      print("\n value is correct")
#     break
# else:
#   while i == length_key - 1:
#      if value[j][i] == word:
#     else:
#        print("\n  Opps!!! value is incorrect")
#       chance = chance - 1
#      print(chance)
#     break
# i += 1
