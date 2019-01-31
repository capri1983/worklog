
fruit = 'banana'
first_names = ['shah', 'sharimen', 'kakachodha']
last = ' sleep'

#index = 0
#while index < len(fruit):
#    print(fruit[index])
#    index += 1

#index = len(fruit) - 1
#while index >= 0:
 #   print(fruit[index])
  #  index -= 1

for char in fruit:
    print(char)

#ls = map(lambda x: x + ' newaz', first_names)
#print(list(ls))

for char in first_names:
    print(char + last)

print(fruit[3])
print(fruit[1:3])
print(fruit[:])

word = 'sharimen'
count = 0
vowels = ['a','e','i','o','u']

for char in word:
    if char in vowels:
        count += 1
    # elif char == 'e':
    #     count += 1
    # elif char == 'i':
    #     count += 1
    # elif char == 'o':
    #     count += 1
    # elif char == 'u':
    #     count += 1

print (count)


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print (letter)


in_both('anwisssss','kakachodha')

