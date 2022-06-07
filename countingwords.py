# Request text from user
text = input("Enter text: ")
# "How many words are there in this text?"

word_list = text.split()
words_count = len(word_list)

print(words_count)