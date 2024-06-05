import src.permutations as permutations
import src.methodStore as methodStore

STATE = {
    'stage' : 0,
    'notation': [],
    'bob' : 0,
    'single' : 0,
    'composition' : [],
    'courseLen' : -1
}

# Take input - keeps taking row crossing till input of 0
def takePlaceNotation():
    if len(STATE['notation']) != 0:
        print("You've already entered the place notation: ")
        print(STATE['notation'])
        if(input("Enter 0 if you wish to cancel\n>> ") == "0"):
            return

    print("Please enter the method's default place notation (enter 0 to finish)")
    print("For each change put in the numbers and press enter")
    exit = False
    while not exit:
        inp = input(">> ")
        if inp == "0":
            exit = True
        elif inp.lower() == "x":
            STATE['notation'].append(-1)
        else:
            try:
                varInt = int(inp)
                STATE['notation'].append(varInt)
            except:
                print("Input not added!\nerror: wrong type")
    print(STATE['notation'])

# Take bobs and singles
def takeBandS():
    # taking bobs
    print("Please enter the bob place notation (enter 0 to finish)")
    inp = input(">> ")
    if inp == "0":
        exit = True
    else:
        try:
            varInt = int(inp)
            STATE['bob'] = varInt
        except:
            print("Input not added!\nerror: wrong type")


    # taking singles
    print("Please enter the single place notation (enter 0 to finish)")
    inp = input(">> ")
    try:
        varInt = int(inp)
        STATE['single'] = varInt
    except:
        print("Input not added!\nerror: wrong type")

    print(STATE['bob'])
    print(STATE['single'])

#Take the composition
def takeComp():
    if len(STATE['composition']) != 0:
        print("You've already entered the STATE['composition']: ")
        print(STATE['composition'])
        if(input("Enter 0 if you wish to cancel\n>> ") == "0"):
            return
    if STATE['courseLen'] == -1:
        courseLen = input("You haven't entered a course length.\n>> ")

    print("Please enter the composition per course end (enter 0 to finish)")
    exit = False
    while not exit:
        inp = input(">> ")
        if inp == "0":
            exit = True
        else:
            try:
                # convert input into int array
                intArr = []
                for x in range (len(str(inp))):
                    intArr.append(int(str(inp)[x]))
                    
                STATE['composition'].append(intArr)
            except:
                print("Input not added!\nerror: wrong type")

    # print composition
    for x in range (len(STATE['composition'])):
        print(STATE['composition'][x])



# Menu for composition writeout
def compWriteMenu():
    #set the stage for the method
    if STATE['stage'] == 0:
        STATE['stage'] = input("Enter the number of bells\n>> ")
    
    print("This is the menu for writing out the method")
    print("Please enter the number of the option you wish to choose:")
    print("     1: enter method default place notation")
    print("     2: enter the bob and single place notation")
    print("     3: enter the composition")
    print("     4: print the changes")
    print("     5: load a method")
    print("     0: Exit")

    # take the option
    userOp = input(">> ")
    if userOp == "1":
        takePlaceNotation()
        compWriteMenu()
    elif userOp == "2":
        takeBandS()
        compWriteMenu()
    elif userOp == "3":
        takeComp()
        compWriteMenu()
    elif userOp == "4":
        permutations.permute(STATE)
    elif userOp == "5":
        loadMethod()
        print(STATE['notation'])
        compWriteMenu()
    elif userOp == "0":
        print("Goodbye!")
    else:
        print("Invalid input: " + userOp)
        compWriteMenu()

def loadMethod():
    # taking method name
    print("Please enter the method you want to load (input 0 to exit):")
    methodStore.printMethods()
    
    inp = input(">> ")
    if inp == "0":
        return
    else:
        try:
            varInt = int(inp)
            STATE['notation'] = methodStore.readMethods(varInt)
        except:
            print("Method not loaded!\nerror: wrong type")