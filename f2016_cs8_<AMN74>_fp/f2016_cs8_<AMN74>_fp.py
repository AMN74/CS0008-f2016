class Participant:

    name = ""
    runs = 0
    distance = 0.0

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getDistance(self):
        return self.distance

    def getRuns(self):
        return self.runs

    def addDistance(self, distance):
        self.distance += distance
        self.runs += 1

    def addDistance(self, list_distance):
        for distance in list_distance:
            self.distance += distance
            self.run += 1

    def __str__(self):
        return_string = "Name: " + self.name + ". Distance Run: " + self.distance + ". Runs: " + self.runs
        return return_string


def processFile(fileIn):
    PTN = 0  #This is the variable for partial total of lines
    PD = 0.0 #This is the variable for the partial distance
    runnerList = {} #variable in which information will be stored to
    dupeList = {} #variable in which information will be stored to

    #Using a for loop we are going remove the the new line in the string (\n) . Then split the data that is given seperating
    # the name from the numerical value (splitting ",". After that we will count the total number of lines and total distance run
    next(fileIn)
    for line in fileIn: #for each line in fileIn
        line = line.rstrip("\n") #we will take each line and remove the new line in the string
        temp = line.split(",") #Then we will split the data from the comma
        name = temp[0] #assigning the indexed information into a variable
        CRD = float(temp[1]) #the current runners distance traveled
        if name in runnerList: #start of a conditional statement to create a counter for the names
            if name in dupeList: #the first time a name appears in a list add to the name counter
                dupeList[name] += 1
            else:
                dupeList[name] = 2 #when a copy of the name appears to the counter do not add to the counter
            if CRD > runnerList[name]:
                runnerList[name] = CRD

        else:
            runnerList[name] = CRD
        PD += CRD #We will add the the total amount of non-numerial values from the data given
        PTN += 1 #We are adding each time the program loops
    return runnerList, dupeList, PTN, PD

#In this function we are taking the key,value, and length.
def printKV(key,value,klen = 0):
    KL = max(len(key), klen)
    FS = ""
    if isinstance(value, str):
        FS = '20s' #here we are telling the program that the string should be 20 spaces long
    elif isinstance(value, float):
        FS = '10.3F' #here we are telling the program that there should be a total of 10 spaces with 3 decimals
    print(format(key, str(KL)+'s'), ':', format(value, FS))  #here we are formatting the key and the value

masterDictionary = {} #creating a master dictionary
masterDupe = {} #creating a dictionary for the duplicated
totalFiles = 0
totalTN = 0 #variable for total lines
totalD = 0 #variable for total distance
fileName = input("Master file input list to be read: ") #prompt the user to which file name needs to be read
masterFileIn = open(fileName) #opening the file

for fileName in masterFileIn: #what to do when the user doesn't type in 'quit'
    totalFiles += 1
    fileName = fileName.rstrip("\n")  # we will take each line and remove the new line in the string
    fileIn = open(fileName) #opening file
    runnerList = {} #creating list for runners in this file
    dupeList = {} # list of duplicate runners in the file
    runnerList, dupeList, PTN, PD = processFile(fileIn)
    masterDictionary.update(runnerList)
    masterDupe.update(dupeList)
    totalTN += PTN #adding the total number of lines
    totalD += PD #adding the total distance
    printKV("Partial Total # of lines", PTN) #printing the partial total number of lines
    printKV("Partial Distance run", PD)   #printing the total partial distance of the run
    print("")

maxDist = max(masterDictionary, key=masterDictionary.get) #getting the max distance from the master dictionary
minDist = min(masterDictionary, key=masterDictionary.get) #geting the minimum distance from the master dictionary

printKV("Total # of Participants", len(masterDictionary)) #getting the length of the master dictionary for the total number of participants


print("Duplicate Runners (Number of duplicates)") #outputting the number of duplicated
for runner in masterDupe:
    printKV(runner,masterDupe[runner])


printKV("Max Distance Run by " + maxDist, masterDictionary[maxDist]) #outputting the runner with the max distance
printKV("Min Distance Run by " + minDist, masterDictionary[minDist]) #outputting the runner with the min distance

print("\nTotals") #This is print 'Totals' and will print a line as well
printKV("Total # of files", totalFiles) #outputting the total number of files
printKV("Total # of lines", totalTN) #Prints the total number of lines
printKV("Total Distance run", totalD) #Prints the total distance run

outFile = open("f2016_cs8_<AMN74>_fp.data.output.csv", "w")
for runner in masterDictionary:
    if runner in masterDupe:
        outFile.write(runner + "," + str(masterDupe[runner]) + "," + str(masterDictionary[runner]))
    else:
        outFile.write(runner + ",1," + str(masterDictionary[runner]))
    outFile.write("\n")
outFile.close()