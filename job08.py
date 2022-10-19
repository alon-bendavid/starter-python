height = int(input("type height of box "))
witdth = int(input("type witdth of box "))



for x in range(height):
    if x < range(height)[1] or x == range(height)[-1]:
     print("|" + witdth * "-"+ "|")
    else:
     print("|" + witdth *" " + "|")     


