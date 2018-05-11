the_file =  open('Result.txt', 'w')

def printPlayerList(l1):
    for x in l1:
        #print('->',x.attributes[0], x.attributes[1], x.attributes[2])
        the_file.write(x.attributes[0] + x.attributes[1] + x.attributes[2]+'\n')
    the_file.write('\n\n')


def combo1(l1, i, temp, t, r, length, lol):
    
    if(t == r):
        lol.append(temp[:])
        return
    if(i >= length):
        return
    
    temp[t] = l1[i]
    combo1(l1, i+1, temp, t+1, r, length, lol)
    combo1(l1, i+1, temp, t, r, length, lol)
    
def combo(l1, r):
    lol = []
    temp = [0]*r
    combo1(l1, 0, temp, 0, r, len(l1), lol)
    return lol


f = open("SumitCricData.csv")

line = f.readline()

attributes = line.strip('\n').split(",")
class Player:
    def __init__(self):
        self.attributes = []    
    pass

allPlayers = []
playerTypesMap = {}

def pushToMap(type, p):
    if type not in playerTypesMap:
        temp = []
    else:
        temp = playerTypesMap[type]
    temp.append(p)
    playerTypesMap[type] = temp;

line = f.readline()

while line:
    parsed = line.strip('\n').split(",")
    p = Player()
    p.attributes.append(parsed[0])
    p.attributes.append(parsed[1].upper())
    p.attributes.append(parsed[2])
    #p.attributes.append(parsed[3])
    allPlayers.append(p)
    pushToMap(parsed[1].upper(), p)
    #print(p.attributes)
    line = f.readline()

playerTypes = ['BAT', 'BOW', 'WK', 'AR']
playerTypesFromInput = list(playerTypesMap.keys())
for item in playerTypes:
    if item in playerTypesFromInput:
        playerTypesFromInput.remove(item)
if(len(playerTypesFromInput)!=0):
    print('Below items are not there in hardcoded list. Update it there')
    print(playerTypesFromInput)
    

print(len(playerTypesMap))

listOfBatsMan = playerTypesMap['BAT']
print('-----',len(listOfBatsMan))
battingCombo = combo(listOfBatsMan, 4)
print(len(battingCombo))

listOfBowlers = playerTypesMap['BOW']
print('-----',len(listOfBowlers))
bowlingCombo = combo(listOfBowlers, 3)
print(len(bowlingCombo))

listOfWKs = playerTypesMap['WK']
print('-----',len(listOfWKs))
wkCombo = combo(listOfWKs, 1)
print(len(wkCombo))


listOfARs = playerTypesMap['AR']
print('-----',len(listOfARs))
arCombo = combo(listOfARs, 3)
print(len(arCombo))

def calculateCredits(l1):
    temp = 0
    for l in l1:
        temp+=float(l.attributes[2])
    return temp

def maxFromSameTeam(l1, noOfTeams):
    temp = 0
    for l in range():
        temp+=float(l.attributes[2])
    return temp


tempCombo =[]
finalList = []
for batsmanList in battingCombo:
    for bowlersList in bowlingCombo:
        for wkList in wkCombo:
            for arList in arCombo:
                tempCombo = wkList + batsmanList + bowlersList  + arList
                if calculateCredits(tempCombo) <= 100:
                    finalList.append(tempCombo[:])




print(len(finalList))

the_file.write('Total Combinations = ' + str(len(finalList))+'\n\n')

for f in finalList:
    printPlayerList(f)
the_file.close()



