class CompExp:
    methodFlip = []
    bob = 0
    single = 0
    composition = []
    stage = -1

    # Take input - keeps taking row crossing till input of 0
    def takeInput(self):
        if self.methodFlip != []:
            print("You've already entered the method flip: ")
            print(self.methodFlip)
            if(input("Enter 0 if you wish to cancel\n>> ") == "0"):
                return

        print("Please enter the method's default crossing order (enter 0 to finish)")
        print("For each change put in the numbers and press enter")
        exit = False
        while not exit:
            inp = input(">> ")
            if inp == "0":
                exit = True
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
        print("Please enter the bob crossing order")
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
        print("Please enter the single crossing order")
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

        print("Please enter the composition per course end (enter 0 to finish)")
        exit = False
        while not exit:
            inp = input(">> ")
            if inp == "0":
                exit = True
            else:
                try:
                    varInt = int(inp)
                    self.composition.append(varInt)
                except:
                    print("Input not added!\nerror: wrong type")
        print(self.composition)

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
        count = 1
        roundsFound = False
        while(count < 10000 and not roundsFound):
            swap = self.methodFlip[count % len(self.methodFlip)]
            print(swap)

            count=count+1
    
    def permuteRow(self, row, swap):
        
        #Split the row and swap into arrays
        prevRow = list(row)
        temp = list(swap)
        
        #Find the bells that are not making a place
        swap = []
        for c in range (int(self.stage)):
            if c+1 not in temp:
                swap.append(c+1)

        #Swap the bells
        newRow = []

        # for count in range(0, len(swap),2):
            # print(swap[count], " ", swap[count+1])

        # should be: 0,2,4,6
        for count in range(0, len(swap),2):
            print(count)
            if(swap[count] == count+1):
                print("here")
                newRow.append(prevRow[swap[count+1]-1])
                newRow.append(prevRow[swap[count]-1])
            else:
                print("else")
                newRow.append(prevRow[count])
                newRow.append(prevRow[count+1])
                count = count - 2
            # print(count)
        print(newRow)

        return newRow
    
    # Menu for composition writeout
    def compWriteMenu(self):
        #set the stage for the method
        if self.stage == -1:
            self.stage = input("Enter the number of bells\n>> ")
        
        print("This is the menu for writing out the method")
        print("Please enter the number of the option you wish to choose:")
        print("     1: enter method default crossing order")
        print("     2: enter the bob and single crossing order")
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
            # print("ife")
            self.takeComp()
            self.compWriteMenu()
        elif userOp == "4":
            # self.permute()
            self.permuteRow([1,2,3,4,5,6,7,8], [3,4])
        elif userOp == "0":
            print("Goodbye!")
        else:
            print("Invalid input: " + userOp)
            self.compWriteMenu()

    def main(self):
        self.compWriteMenu()

if __name__ == '__main__':
    CompExp().main()