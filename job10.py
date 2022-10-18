#ask for a text

text = str(input("please type a random text "))
path_txt = r"C:\Users\PX229\Desktop\laplateforme\starter-python\job10-text\readme.txt"

#open a text file named "output.txt"

with open(path_txt, 'w') as file:
    file.write(text)
    
#read the text file that you have just opend and print it to terminal

print(file.read())