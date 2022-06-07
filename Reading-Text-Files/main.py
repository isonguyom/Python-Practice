# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from posixpath import split


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as open_file:
        read_file = open_file.read()
    
    return read_file


def count_words(filename):
    text = read_file_content(filename)
    # [assignment] Add your code her
    
    split_text = text.split()
    
    count_each_word = {}
    for i in split_text:
        if i in count_each_word:
            count_each_word[i] += 1
        else:
            count_each_word[i] = 1

    return count_each_word
    


print(count_words("python\Reading-Text-Files\story.txt"))