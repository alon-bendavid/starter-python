#number of bricks for height and floor
bricks = int(input("type number of bricks "))

#space outside of the pyrmide
space = bricks

#space inside pyrmide
midspace = 0

#pyrmide structure

for x in range(bricks):
    if x != bricks:
        
        print(space*" "  + "/" + midspace*" " + "\ " )
    midspace += 2
    space -= 1
    x += 1
    if x == bricks:
        print(space*" "  + "/"+ midspace*"_"+ "\ " )


