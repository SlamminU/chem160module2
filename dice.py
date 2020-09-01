from random import choices
nrolls=10000
total=0
ndice=6
for i in range(nrolls):
    dice=choices(range(1,7),k=ndice)
    dice.sort(reverse=True)
    dice=choices(range(1,7),k=ndice)
print("Average roll=",total/nrolls)