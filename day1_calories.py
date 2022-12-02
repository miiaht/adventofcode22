
newlist = []
counter = -1
newsum = 0

with open('day_1_input_list.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip("\n")
    if line == "":
        counter += 1
        newsum = 0
    else:
        newsum+= int(line)
        newlist.append(newsum)

#Task 1: Find the total sum of calories carried by the elf with the most calories with them.
print(max(newlist))
#Task 2: Find the total sum of the top 3 elves carrying the most calories
newlist.sort(reverse=True)
print(sum(newlist[0:3]))

