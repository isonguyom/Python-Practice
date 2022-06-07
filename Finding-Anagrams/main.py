# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
first_word = input("Enter first word: ")
compare_word = input("Enter second word: ")

def find_anagram(word, anagram):
    # [assignment] Add your code here
    # conver string to list
    word = list(word)
    anagram = list(anagram)

    # Sort lists
    word.sort()
    anagram.sort()

    # Compare word and anagram
    if word == anagram:

        print(True)
    else:
        print(False)
    


find_anagram(first_word, compare_word)
# find_anagram("hello", "check")