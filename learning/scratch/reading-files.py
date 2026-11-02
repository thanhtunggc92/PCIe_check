with open("learning/scratch/temps.txt") as f:
    temp= f.read()


# print(temp.split())
# print(temp.splitlines())
name=[]
for i in temp.split():
    if str(i).isalpha():
        name.append(i)

print(name)