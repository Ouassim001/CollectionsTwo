
# def names():
#     TotalNames = []
#     name1 = input("what is your name?\n")
    


    
#     if name1 in TotalNames:
#         change1 = input("change name here\n")
#         TotalNames.append(change1)
#     else:
#         TotalNames.append(name1)
#         name2 = input("what is your name?\n")



#     print(TotalNames)




# names()







# # elif name2 in TotalNames:
# #         change2 = input("change name here\n")
# #         TotalNames.append(change2)




# # hieronder is eerste kerstlootjes.py
# def names():
#     name1 = input("what is your name?\n")
#     name2 = input("what is your name?\n")
#     TotalNames = []

#     TotalNames.append(name1)
#     TotalNames.append(name2)
    
    
#     print(TotalNames)

# names()




#  name1 = input("what is your name?\n")
#     TotalNames.append(name1)
    
#     name2 = input("what is your name?\n")
#     TotalNames.append(name2)

#     name3 = input("what is your name?\n")
#     TotalNames.append(name3)

#     name4 = input("what is your name?\n")
#     TotalNames.append(name4)

#     print(TotalNames)



# import random
# global colours 
# global current
# colours = ["Red","Yellow","Blue","Green","Orange","White"]
# current = []

# def randompicker():
#     for i in range(4):
#         current = random.choice(colours)
# randompicker()
# print(colours)
# print(current)




# create a list
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)