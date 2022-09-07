import random
listnummers = [1,2,3,4,5,6,7,8,9,10]
listkaarten = ["harten", "klaveren", "schoppen", "ruiten"]
listspecials = ["boer", "vrouw", "heer", "aas", "joker"]
list = []
for i in listkaarten:
    for j in listnummers:
        list2 = str(i) + " " + str(j)
        list.append(list2)
        for k in listspecials:
            list2special = str(i) + " " + str(k)
            list.append(list2special)
for l in range(7):
    x = random.choice(list)
    print(x)
print(list)
