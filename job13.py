import re
#import file
file = open(r"C:\Users\PX229\Desktop\laplateforme\starter-python\job12_file\data.txt")

#ask for a whole number
word_len = int(input('Plese enetr size of word :'))

#brake file into words
data = file.read()
words = data.split()
count = 0
for word in words:
    if len(word) == word_len:
        count += 1
print("Number of words that size is:",count) 

