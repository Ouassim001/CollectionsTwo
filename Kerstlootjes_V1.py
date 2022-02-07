import random
TotalNames = []

def names():
    name = []
    for i in range(4):
        while True:
            name = input("what is your name\n").lower()
            if name in TotalNames:
                print("Name already in")
            else:
                TotalNames.append(name)
                break

    lots = [1,2,3,4]
    score = []
    x = random.choice(lots)
    random1 = score.append(x)
    random2 = random.shuffle(name)
    var1 = str(name[0]) + str(score[0])
    print(var1)

    var2 = str(name[1] + str(score[1]))
    print(var2)
    

    
    # score2 = [random1,name]
    # random2 = print(score2.append(TotalNames))
    # print(score2)

    # print(TotalNames.extend([score]))
    # print(dict)
    



    




names()
# print(TotalNames)