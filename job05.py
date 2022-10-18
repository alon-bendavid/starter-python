vala = int(input("enter value A "))
valb = int(input("enter value B "))

#in case values are equals
if vala == valb:
    print("Valeurs égales")
    
#print values from lower to higher    
if vala < valb:
 numbers = range(vala+1,valb)
 for x in numbers:
     print(x) 

#print values from higher to lower 
elif vala > valb:
 numbers = range(vala-1,valb, -1)
 for x in numbers:
     print(x) 


 
         




