class CompExp:
    methodFlip = []
    bob = 0
    single = 0
    composition = []

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
                    self.methodFlip.append(inp)
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
                self.bob = inp
            except:
                print("Input not added!\nerror: wrong type")

        # taking singles
        print("Please enter the single crossing order")
        inp = input(">> ")
        if inp == "0":
            exit = True
        else:
            try:
                varInt = int(inp)
                self.single = inp
            except:
                print("Input not added!\nerror: wrong type")

        print(self.bob)
        print(self.single)

    #Write out the method
    def permute(self):
        numbers = input("Enter the number of bells\n>> ")
        
        num = 0
        
        try:
            num = int(numbers)
        except:
            print("Cannot convert" + numbers + " to an integer")

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

    # Menu for composition writeout
    def compWriteMenu(self):
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