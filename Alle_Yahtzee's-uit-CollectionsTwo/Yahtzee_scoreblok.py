scores = [5,6,31,4,0]

titles = ["small straight", "large staright", "three of a kind", "four of a kind", "Full house"]


for s in range(5):
    print()
    print(" {:20}  :  |_-_|".format(titles[s]) + "{:2} |_-_|".format(scores[s]))
       



print("cijfers:  |" + ("xyz |" * 10))


print("cijfers:  |" + ("{:2} |" * 10).format(*scores))

print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))