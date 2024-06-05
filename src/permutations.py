#Write out the method
def permute(STATE):
    num = 0
    
    try:
        num = int(STATE['stage'])
    except Exception as e:
        raise SyntaxError(f"Cannot convert {STATE['stage']} to an integer")

    permutations = [[]]

    #set rounds
    for x in range (num):
        permutations[0].append(x+1)
    
    #swap each row
    count = 0
    roundsFound = False

    # trackers for composition
    course = 0
    inc = 0

    while(count < 10000 and not roundsFound):
        stationaryBells = STATE['notation'][count % len(STATE['notation'])]
        #if all bells cross
        if stationaryBells == -1:
            permutations.append(permuteRow(permutations[count], []))
        else:
            permutations.append(permuteRow(permutations[count], stationaryBells))

        count=count+1

        #Working out a lead end
        if isLeadEnd(permutations):
            print("is the lead end")

        #exit condition
        if(permutations[count] == permutations[0]):
            roundsFound = True

        


def permuteRow(row, swap):
    #Split the row and swap into arrays
    
    #covert swap to array of chars
    if swap != []:
        temp = str(swap)
        swapArr = []
        for x in temp:
            swapArr.append(int(x))
    else:
        swapArr = []

    # print("swap: " + str(swapArr))

    #Swap the bells
    newRow = []

    x = 0
    while x < (len(row)):
        #If bell makes place
        if x+1 in swapArr:
            newRow.append(row[x])
        #Otherwise, swap
        else:
            x += 1
            newRow.append(row[x])
            newRow.append(row[x-1])
        x += 1
    print(newRow)
    return newRow



def isLeadEnd(permutations):
    if len(permutations) > 2:
        # The "bob" row will be calculated without the bob, so we need to ignore it
        backOne = permutations[-1]
        backTwo = permutations[-2]
        
        # print(backOne)
        # print(backTwo)
        
        if backOne[0] == 1 and backTwo[0] == 1:
            return True
    
    return False