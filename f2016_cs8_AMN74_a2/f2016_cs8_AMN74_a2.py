#Students are to write a python program that address the problem describe below under the description
#section.
#Students will need to commit the assignment in their git repository under a new folder named:
#• f2016_cs8_<pitt-username>_a2
#<pitt-username> needs to be substituted with the student pitt username. My pitt username is man8, so
#my folder will be named f2016_cs8_man8_a2.
#Inside the assignment folder, students have to commit at least the following three files:
#• f2016_cs8_<pitt-username>_a2.readme.txt:
#simple text file describing the thought process that was used to write the program.
#• f2016_cs8_<pitt-username>_a2.py
#python program
#• f2016_cs8_<pitt-username>_a2.run1.txt:
#simple text file containing one test run of the program. It has to show input provided by the user
#and output produced by the program. This file is going to be used by the instructors to test the
#code and will contribute to the assignment grade. If the student wold like to submit multiple test
#files, he/she should commit more changing run1 to run2 and so forth.
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
#• Instructors will grade the last commit before midnight of Friday 2016/10/28.
#• Do not wait the last minute to commit.
#• Please commit your work-in-progress as many time as you can.
#• No late commits, no extensions (unless previously agreed).
#• Do not be afraid to ask question and search examples
#• Two test files are provided on CourseWeb:
#f2016_cs8_a2.data.1.csv and f2016_cs8_a2.data.2.csv
#Page 1 of 3
#CS 0008 – Fall 2016 Assignment #2 Due: 2016/10/28
#Description
#Write a program that loops indefinitely asking the user to enter the name of a text file that is structured
#as it follows:
#Max,34.23
#Barbara,23.00
#Luka,12.87
#…
#Each row is composed by two fields: name and distance run.
#Once you have the name of the file, you have to loop on all the lines, counting how many lines you
#have in each file and providing a running tally on how much is the total distance run.
#You need to provide the partials for each file and the overall total encompassing all the files. Output
#format must follow these guide lines:
#File to be read: file_1.csv
#Partial Total # of lines : x1
#Partial distance run : y1
# File to be read: file_2.csv
#Partial Total # of lines : x2
#Partial distance run : y2
# File to be read: quit
#Totals
#Total # of lines : x1 + x2
#Total distance run : y1 + y2
#Length of each label is left to the programmer discretion, as long as it looks pleasant and acceptable.
#The program should loop indefinitely until the user enters an empty string, the word “quit” or the letter
#“q”.
#In your program, you should define at least the following two functions:
#• processFile(fh)
#This function accept one argument in input that is the handle to the file object to be read. It
#returns 2 values: the first is how many lines the file has and the second is the total sum of the
#distance of each record
#Page 2 of 3
#CS 0008 – Fall 2016 Assignment #2 Due: 2016/10/28
#• printKV(key,value,klen = 0)
#This function accept in input 2 mandatory arguments: key and value and an optional third
#klen, aka key length. If klen is not passed when called, it defaults to 0.
#The function does not return any value.
#The functionality provided by the function printKV is to print key and value in a consistent
#format. First, it prints the key as n-length characters string where n is the max between length
#of key and the value of klen. It than insert “ : “ followed by the formatted representation of the
#value. Format of value changes according to the type of the value contained in the variable.
#Here are the case defined by the client/user:
#• string: it should be 20 spaces long,
#• float: it should be a total of 10 spaces with 3 decimals
#• integer: it should be 10 spaces
#Cases not covered in the previous list, are left to the programmer to decide which is the best
#behavior to implement.
#Additional informations:
#• use a for loop to read lines from the file
#• use rstrip method to remove the ‘\n’ (new line) from the end of each line read.
#• use split method to separate names from distance in each line read from file.
#• use the function isinstance to test if a variable contains a string, a float or an integer
#• do not forget to open and close every file and select the right mode when opening


# MN: what does this function do?
def processFile(fileIn):
    PTN = 0  #This is the variable for partial total of lines
    PD = 0.0 #This is the variable for the partial distance

    # MN: respect the indentation with comment too
    # Using a for loop we are going remove the the new line in the string (\n) . Then split the data that is given seperating
    # the name from the numerical value (splitting ",". After that we will count the total number of lines and total distance run
    for line in fileIn: #for each line in fileIn
        line = line.rstrip("\n") #we will take each line and remove the new line in the string
        temp = line.split(",") #Then we will split the data from the comma
        PD += float(temp[1]) #We will add the the total amount of non-numerial values from the data given
        PTN += 1 #We are adding each time the program loops
    return PTN, PD

#In this function we are taking the key,value, and length.
def printKV(key,value,klen = 0):
    KL = max(len(key), klen)
    FS = ""
    if isinstance(value, str):
        FS = '20s' #here we are telling the program that the string should be 20 spaces long
    elif isinstance(value, float):
        FS = '10.3F' #here we are telling the program that there should be a total of 10 spaces with 3 decimals
    print(format(key, str(KL)+'s'), ':', format(value, FS))  #here we are formatting the key and the value

totalTN = 0 #variable for total lines
totalD = 0 #variable for total distance
fileName = input("File to be read: ") #prompt the user to which file name needs to be read
# MN: what about q and empty string?
while fileName != "quit": #what to do when the user doesn't type in 'quit'
    fileIn = open(fileName)
    PTN, PD = processFile(fileIn)
    totalTN += PTN #adding the total number of lines
    totalD += PD #adding the total distance
    printKV("Partial Total # of lines: ", PTN) #printing the partial total number of lines
    printKV("Partial Distance run: ", PD)   #printing the total partial distance of the run
    print("")
    fileName = input("File to be read: ") #Prompts the user to which file needs to be read
print("\nTotals") #This is print 'Totals' and will print a line as well
printKV("Total # of lines: ", totalTN) #Prints the total number of lines
printKV("Total Distance run: ", totalD) #Prints the total distance run

