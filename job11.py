import re
#path to xml file
path_txt = r"C:\Users\PX229\Desktop\laplateforme\starter-python\job11 domains file\domains.xml"
#open xml file
with open(path_txt,'r') as file:
#look for domain pattern   
    #print(file.read())
    domains = re.findall(r'(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))', file.read())  
    #count and print number of paterns 
    print(len(domains))
   
    