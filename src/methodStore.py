def readMethods(desiredMethod):
    try:
        methods = open("./src/methodStore.txt", "r")

        #return notation of selected method
        count=0
        for item in methods.readlines():
            notation = item.split(" ")[1]
            if count == desiredMethod-1:
                temp = notation.split(":")
                return [eval(i) for i in temp]
            count+=1
    except:
        print("File not found")



def printMethods():
    # methods = 0
    try:
        methods = open("./src/methodStore.txt", "r")
        count = 1
        for item in methods.readlines():
            print(f"    {count}.  {item.split(" ")[0].replace("-", " ")}")
            count+=1
    except:
        print("File not found")



def setStage(desiredMethod):
    try:
        methods = open("./src/methodStore.txt", "r")

        #return notation of selected method
        count=0
        for item in methods.readlines():
            if count == desiredMethod-1:
                name = item.split(" ")[0]
                nameComponents = name.split("-")
                stage = nameComponents[-1]

                match stage:
                    case "Singles":
                        return 3
                    case "Minimus":
                        return 4
                    case "Doubles":
                        return 5
                    case "Minor":
                        return 6
                    case "Triples":
                        return 7
                    case "Major":
                        return 8
                    case "Caters":
                        return 9
                    case "Royal":
                        return 10
                    case "Cinques":
                        return 11
                    case "Maximus":
                        return 12
                    case "Sextuples":
                        return 13
                    case "Fourteen":
                        return 14
                    case "Sixteen":
                        return 16
            count+=1
    except:
        print("File not found")
