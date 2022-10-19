
#import file
file = open(r"C:\Users\PX229\Desktop\laplateforme\starter-python\job12_file\data.txt")
#brake file into words
data = file.read()
words = data.split()
#count and print
print('number of words :', len(words))


