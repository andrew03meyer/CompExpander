class CompExp:
    methodFlip = []
    bob = 0
    single = 0
    composition = []
    stage = -1
    courseLen = -1

    # Take input - keeps taking row crossing till input of 0
    def takeInput(self):
        if self.methodFlip != []:
            print("You've already entered the place notation: ")
            print(self.methodFlip)
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
                self.methodFlip.append(-1)
            else:
                try:
                    varInt = int(inp)
                    self.methodFlip.append(varInt)
                except:
                    print("Input not added!\nerror: wrong type")
        print(self.methodFlip)

    # Take bobs and singles
    def takeBandS(self):
        # taking bobs
        print("Please enter the bob place notation (enter 0 to finish)")
        inp = input(">> ")
        if inp == "0":
            exit = True
        else:
            try:
                varInt = int(inp)
                self.bob = varInt
            except:
                print("Input not added!\nerror: wrong type")

        # taking singles
        print("Please enter the single place notation (enter 0 to finish)")
        inp = input(">> ")
        try:
            varInt = int(inp)
            self.single = varInt
        except:
            print("Input not added!\nerror: wrong type")

        print(self.bob)
        print(self.single)

    #Take the composition
    def takeComp(self):
        if self.composition != []:
            print("You've already entered the composition: ")
            print(self.composition)
            if(input("Enter 0 if you wish to cancel\n>> ") == "0"):
                return
        if self.courseLen == -1:
            self.courseLen = input("You haven't entered a course length.\n>> ")

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
                        
                    self.composition.append(intArr)
                except:
                    print("Input not added!\nerror: wrong type")

        # print composition
        for x in range (len(self.composition)):
            print(self.composition[x])

    #Write out the method
    def permute(self):
        num = 0
        
        try:
            num = int(self.stage)
        except:
            print("Cannot convert" + self.stage + " to an integer")

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
            # if there is no call
            if (self.composition[course][inc] != inc):
                swap = self.methodFlip[count % len(self.methodFlip)]
                if swap == -1:
                    permutations.append(self.permuteRow(permutations[count], []))
                else:
                    permutations.append(self.permuteRow(permutations[count], swap))

                count=count+1
                

            #exit condition
            if(permutations[count] == permutations[0]):
                roundsFound = True

            
    

    def permuteRow(self, row, swap):
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
            if x+1 in swapArr:
                newRow.append(row[x])
            else:
                x += 1
                newRow.append(row[x])
                newRow.append(row[x-1])
            x += 1
        print(newRow)
        return newRow
    
    # Menu for composition writeout
    def compWriteMenu(self):
        #set the stage for the method
        if self.stage == -1:
            self.stage = input("Enter the number of bells\n>> ")
        
        print("This is the menu for writing out the method")
        print("Please enter the number of the option you wish to choose:")
        print("     1: enter method default place notation")
        print("     2: enter the bob and single place notation")
        print("     3: enter the composition")
        print("     4: print the changes")
        print("     0: Exit")

        # take the option
        userOp = input(">> ")
        if userOp == "1":
            self.takeInput()
            self.compWriteMenu()
        elif userOp == "2":
            self.takeBandS()
            self.compWriteMenu()
        elif userOp == "3":
            self.takeComp()
            self.compWriteMenu()
        elif userOp == "4":
            self.permute()
        elif userOp == "0":
            print("Goodbye!")
        else:
            print("Invalid input: " + userOp)
            self.compWriteMenu()

    def main(self):
        self.compWriteMenu()

if __name__ == '__main__':
    CompExp().main()