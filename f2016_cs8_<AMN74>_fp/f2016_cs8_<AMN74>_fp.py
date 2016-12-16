#
#
# name       : Amulia Nambiar
# email      : AMN74@pitt.edu
# date       : 2016/12/15
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Final Project
#
# Description:
# A customer needs to process a number of text files (called data files) that contain names and distance run by study participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
# …
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …
#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the following
# quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	Total number of participants : xx
#	Number of participants
#    with multiple records       : xx
#
# The program should also create an output file reporting name of the participant, how many times their name appears in
# the input files and the total distance run. Each row should be as follows:
#
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87
# …
#
# In this program, the student should make the best use of everything that has learn so far in this class,
# reuse as much as he/she can from assignment #3, improve upon it and he/she has to use a class named participants
# that has 3 properties:
# - name: name of the participant. String.
# - distance: accumulator for total distance run by the participant. Float.
# - runs: accumulator for the total number of runs run by the participant.
#
# and, at least, the following methods:
# - addDistance(d)
#   add single distance to the distance accumulator and increments runs by 1. Argument d is a single float.
# - addDistances(ld)
#   add an array of distances to distance accumulator. Argument ld is a list of floats. getDistance()
#   get the current value of the distance accumulator.
# - getName()
#   get the name of the participant of the current instance
# - getDistance()
#   get the total distance run computed
# - getRuns()
#   get the total number of runs
# - __init__ (n,d=0)
#   initializer method. set name and initial distance if provided. If initial distance is not specified,
#   it should be set to zero
# - __str__()
#   stringify method. Returns a string with name, total distance run and how many distances the object added,
#   according to the following format:
#   Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
#
#   where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name,
#   yyyy.yyyy is the total distance run with 9 digits, decimal point and 4 decimals,
#   and zzzz is the number of runs with 4 digits, no decimals.
#

#The start of my final project python file:

#First I defined a class
class Participant:
    #here I get the name of the participant
    name = ""
    #here is the total number of runs by the participant
    runs = 0.0
    #here is the total distance by the participant
    distance = 0.0

    #here I define the following methods the program can use
    #the first method I am defining is the initializing method in this method I am adding 2 arguments
    def __init__(self, name, distance= 0):
        #here I am setting the name within the method (1st argument)
        self.name = name
        #here I am using a conditional statement if the distance is greater than zero
        if distance > 0:
            #here we are setting the distance within the method (2nd argument)
            self.distance = distance
            #here we are setting the number of runs
            self.runs = 1
        #conditional statement ends
    #end of the initializing method

    #Here I am defining a method that will add a single distance to a distance accumulator and increment the runs by 1
    def addDistance(self, distance):
        #here I am using a conditional statement so that the program knows what to do if the distance is greater and 0
        if distance > 0:
            self.distance += distance
            self.runs += 1
        # the is the end of the conditional statement
    #this is the end of the method that will add a single distance to a distance accumulator and increment the runs by 1

    # here I am defining a method that will add an array of distances to the distance accumulator
    def addDistances(self, distances):
        # Here I am looping over all of the items in the list
         for distance in distances:
            # here I am using a conditional statement if the distance is greater than zero
            if distance > 0:
                self.distance += distance
                self.runs += 1
            # here is the end of the conditional statement
        # here is the end of the for loop
    # here is the end of the method that adds a single distance to the distance accumulator and will increment the runs by 1

    #here I am defining a method that will get the name of the participant at this instance
    def getName(self):
        return self.name
    #end of the method that will get the name of the participant in this instance

    #here I am telling the program to return the value from the distance accumulator
    def getDistance(self):
        return self.distance
    #end of the method that will return the calculated value of the total distance run

    #here I am defining a method that will return the total number of runs
    def getRuns(self):
        return self.runs
    #end of the method that will return the total number of runs

    #here I am defining a string method that returns the name, total distance run, as well as the total runs
    def __str__(self):
        return_string = "Name: " + format(self.name, '>20s')+ ". Total distance Run: " + format(self.distance, '9.4f') + \
        ". Runs: " + format(self.runs, '4d')
        return return_string
    #end of method that returns the string

#here I am defining a fuction that reads all of the lines of the inputed file
def processFile(fileIn):

    # This is the variable for partial total of lines
    PTN = 0
     # This is the variable for the partial distance
    PD = 0.0
    # empty list in which the participants will be stored
    participantList = []
    # empty list in which the runners will be stored
    runnerList = {}
    # empty list in which the runners will be stored
    dupeList = {}

    #By using a for loop we are going remove the the new line in the string (\n) . Then split the data that is given seperating
    #the name from the numerical value (splitting ",". After that we will count the total number of lines and total distance run
    next(fileIn)
    # for each line in fileIn
    for line in fileIn:
        # we will take each line and remove the new line in the string
        line = line.rstrip("\n")
        # Then we will split the data from the comma
        temp = line.split(",")
        # assigning the indexed information into a variable
        name = temp[0]
        # the current runners distance traveled
        CRD = float(temp[1])
        # start of a conditional statement to create a counter for the names
        if name in runnerList:
            #here I use a for loop to loop over all the runners in the participant list
            for runner in participantList:
                if (runner.getName() == name):
                    runner.addDistance(CRD)
                    break

        else:
            participantList.append(Participant(name, CRD))
            runnerList[name] = CRD
        # We will add the the total amount of non-numerial values from the data given
        PD += CRD
        # We are adding each time the program loops
        PTN += 1
    #We are telling the function to return all of the variables we have defined
    return participantList, runnerList, dupeList, PTN, PD

#In this function we are taking the key,value, and length.
def printKV(key,value,klen = 0):
    KL = max(len(key), klen)
    FS = ""
    if isinstance(value, str):
        # here we are telling the program that the string should be 20 spaces long
        FS = '20s'
    elif isinstance(value, float):
        # here we are telling the program that there should be a total of 10 spaces with 3 decimals
        FS = '10.3F'
    # here we are formatting the key and the value
    print(format(key, str(KL)+'s'), ':', format(value, FS))

#creating a list of all the participants
masterParticipants = []
#creating a master dictionary
masterDictionary = {}
#creating a dictionary for the duplicated
masterDupe = {}
totalFiles = 0
#variable for total lines
totalTN = 0
#variable for total distance
totalD = 0
#prompt the user to which file name needs to be read
fileName = input("Master file input list to be read: ")
masterFileIn = open(fileName) #opening the file
#here I use a for loop to go over all of the file names in the master file
for fileName in masterFileIn:
    totalFiles += 1
    # we will take each line and remove the new line in the string
    fileName = fileName.rstrip("\n")
    # opening file
    fileIn = open(fileName)
    participantList = []
    # creating list for runners in this file
    runnerList = {}
    # list of duplicate runners in the file
    dupeList = {}
    participantList, runnerList, dupeList, PTN, PD = processFile(fileIn)
    masterParticipants += participantList
    masterDictionary.update(runnerList)
    masterDupe.update(dupeList)
    # adding the total number of lines
    totalTN += PTN
    # adding the total distance
    totalD += PD
    # printing the partial total number of lines
    printKV("Partial Total # of lines", PTN)
    # printing the total partial distance of the run
    printKV("Partial Distance run", PD)
    print("")
    #here we close the fileIn
    fileIn.close()
#getting the max distance from the master dictionary
maxDist = max(masterDictionary, key=masterDictionary.get)
#geting the minimum distance from the master dictionary
minDist = min(masterDictionary, key=masterDictionary.get)

#getting the length of the master dictionary for the total number of participants
printKV("Total # of Participants", len(masterDictionary))
#outputting the runner with the max distance
printKV("Max Distance Run by " + maxDist, masterDictionary[maxDist])
#outputting the runner with the min distance
printKV("Min Distance Run by " + minDist, masterDictionary[minDist])

#This is print 'Totals' and will print a line as well
print("\nTotals")
#outputting the total number of files
printKV("Total # of files", totalFiles)
# Prints the total number of lines
printKV("Total # of lines", totalTN)
#Prints the total distance run
printKV("Total Distance run", totalD)


#Here I tell the program to create an output file

#In order to do this I defined a variable that will open the output file and write the name of the participant, how many times their
#name appeared in the input files and the total distance run

outFile = open("f2016_cs8_<AMN74>_fp.data.output.csv", "w")



#here we define the duplicate names
dupePersons = 0

#here the program is looping through all the runners(participants) in the master Participants dictionary
for runner in masterParticipants:
    if (runner.getRuns() > 1):
        dupePersons += 1
    #here I am telling the program what to write into the output file
    outFile.write((runner.getName()) + "," + str(runner.getRuns()) + "," + str(runner.getDistance()) + '\n')


#here I close the output file
outFile.close()
#prints the total duplicates
printKV("Total Dupes", dupePersons)

#end of program