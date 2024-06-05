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