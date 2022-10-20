
def listFunc(*arg):
 my_list = []

 for i in range(len(my_list)):
    print(range(len(my_list)))
    for j in range(i + 1, len(my_list)):

        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

    print(my_list)

listFunc(6 , 4 , 5 , 11 , 35 , 2)    

    


