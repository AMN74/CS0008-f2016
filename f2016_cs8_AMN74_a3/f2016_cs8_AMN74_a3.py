#CS 0008 – Fall 2016 Assignment #3 Due: 2016/11/18
#CS 0008 - Introduction to programming with Python
#Fall 2016
#Assignment #3
#Available: 2016/11/15. Due: 2016/11/18 before midnight.
#Students are to write a python program that address the problem describe below under the description
#section.
#Students will need to commit the assignment in their git repository under a new folder named:
#• f2016_cs8_<pitt-username>_a3
#<pitt-username> needs to be substituted with the student pitt username. My pitt username is man8, so
#my folder will be named f2016_cs8_man8_a3.
#Inside the assignment folder, students have to commit at least the following three files:
#• f2016_cs8_<pitt-username>_a3.readme.txt:
#simple text file describing the thought process that was used to write the program.
#• f2016_cs8_<pitt-username>_a3.py
#python program
#• f2016_cs8_<pitt-username>_a2.run1.txt:
#simple text file containing one test run of the program. It has to show input provided by the
#user, if present and output produced by the program. This file is going to be used by the
#instructors to test the code and will contribute to the assignment grade. If the student wold like
#to submit multiple test files, he/she should commit more changing run1 to run2 and so forth.
#Program has to be in python version 3.x and they will be graded according the following factors:
#• submissions:
#Files and folder has been submitted with correct naming.
#• run:
#Python script runs correctly with python 3.x. Correct output.
#• logic:
#Program follow simple logic. Missing or extra functionalities. Redundant code.
#• beautification:
#Comments, readability, code spacing and organization
#IMPORTANT:
#• Instructors will grade the last commit before midnight of Friday 2016/11/18.
#• Do not wait the last minute to commit.
#• Please commit your work-in-progress as many time as you can.
#• No late commits, no extensions (unless previously agreed).
#• Do not be afraid to ask question and search examples
#• Four test files are provided on CourseWeb: f2016_cs8_a3.data.txt, f2016_cs8_a3.data.1.csv,
#f2016_cs8_a3.data.2.csv, and f2016_cs8_a3.data.3.csv
#Page 1 of 3
#CS 0008 – Fall 2016 Assignment #3 Due: 2016/11/18
#Description
#A customer needs to process a number of text files (called data files) that contain names and distance
#run by study participants. The format of those files is as follows:
#Max,34.23
#Barbara,23.00
#Luka,12.87
#…
#In those files, each row is a comma separated list of 2 values: the first one is the name of the participant
#and the second is the distance that the participant has run.
#The names of the input files are stored one per line in an additional file, called the master input list.
#This file has the following structure:
#<data file 1>
#<data file 2>
#<data file 3>
#…
#Write a program that read the master input list file, retrieves the names of the data files and from each
#one of them reads every line, extract name and distance. Once the program has all the data in memory,
#it has to compute the following quantities and informations:
#• number of files read in input
#• total number of lines read
#• total distance run (aka the sum of all the distances loaded from provided files)
#• total distance run for each individual participant
#• individual maximum distance run and by which participant
#• individual minimum distance run and by which participant
#• report if there are any participants that appears more than once, how many times and their
#names
#• total number of participants
#The program should provide an terminal output similar to the following:
#Number of Input files read : xx
#Total number of lines read : xx
#total distance run : xxxx.xxxxx
#max distance run : xxxx.xxxxx
# by participant : participant name
#Page 2 of 3
#CS 0008 – Fall 2016 Assignment #3 Due: 2016/11/18
#min distance run : xxxx.xxxxx
# by participant : participant name
#Total number of participants : xx
#Number of participants
 #with multiple records : xx
#The program should also create an output file reporting name of the participant, how many times their
#name appears in the input files and the total distance run. Each row should be as follows:
#Max,3,124.23
#Barbara,2,65.00
#Luka,1,12.87
#…
#A zip file named f2016_cs8_a3.data.zip is provided with this assignment. It contains the following
#additional files that are to be used to test assignment #3:
#• f2016_cs8_a3.data.txt: master input list
#• f2016_cs8_a3.data.1.csv: data file 1
#• f2016_cs8_a3.data.2.csv: data file 2
#• f2016_cs8_a3.data.3.csv: data file 3
#The output file mentioned above, that has to be created by the student program, should be named:
#• f2016_cs8_<username>_a3.data.output.csv
#In this program, the student should make the best us of everything that has learn so far in this class:
#functions, for loops, while loops, lists, sets and dictionaries.
#Page 3 of 3

#
# Notes:
# MN: please do not use inline comments. It makes it really hard to read the code

# MN: what does this function do?
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
            # MN: shouldn't you add the current distance to the previous ones?
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
    # MN: where do you close fileIn?
    fileIn.close()

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
