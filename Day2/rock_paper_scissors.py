import re

myScore = 0
#Task 1: Calculate your total score. A-C are oppponent's choices, X-Z are yours. A & X = rock, Y & B = paper, Z & C = scissors.
with open('example.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip("\n")
    listToSplit = re.split(" ", line)
    if listToSplit[0] == "A" and listToSplit[1] == "X":
       myScore +=4
    if listToSplit[0] == "A" and listToSplit[1] == "Y":  
        myScore +=8
    if listToSplit[0] == "A" and listToSplit[1] == "Z":      
        myScore += 3
    if listToSplit[0] == "B" and listToSplit[1] == "X":
       myScore +=1
    if listToSplit[0] == "B" and listToSplit[1] == "Y":  
        myScore +=5
    if listToSplit[0] == "B" and listToSplit[1] == "Z":      
        myScore += 9
    if listToSplit[0] == "C" and listToSplit[1] == "X":
       myScore +=7
    if listToSplit[0] == "C" and listToSplit[1] == "Y":  
        myScore +=2
    if listToSplit[0] == "C" and listToSplit[1] == "Z":      
        myScore += 6        
print(myScore)

#Task 2: X = round needs to end in a Loss  Y = round needs to end in a Draw   Z = round needs to end in a Win. Calculate your total score.
for line in lines:
    line = line.strip("\n")
    listToSplit = re.split(" ", line)
    if listToSplit[0] == "A" and listToSplit[1] == "X":
       myScore +=3
    if listToSplit[0] == "A" and listToSplit[1] == "Y":  
        myScore +=4
    if listToSplit[0] == "A" and listToSplit[1] == "Z":      
        myScore +=8 
    if listToSplit[0] == "B" and listToSplit[1] == "X":
       myScore +=1
    if listToSplit[0] == "B" and listToSplit[1] == "Y":  
        myScore +=5
    if listToSplit[0] == "B" and listToSplit[1] == "Z":      
        myScore +=9 
    if listToSplit[0] == "C" and listToSplit[1] == "X":
       myScore +=2
    if listToSplit[0] == "C" and listToSplit[1] == "Y":  
        myScore +=6
    if listToSplit[0] == "C" and listToSplit[1] == "Z":      
        myScore +=7       

print(myScore)








