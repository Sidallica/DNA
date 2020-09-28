import csv
from sys import argv, exit


def main():

   # Checking for correct number of command line arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Opening first CL argument contraining STR Database
    with open(argv[1], "r") as csvfile:

        # Reading contents of CSV into a dictionary
        STRdb = list(csv.DictReader(csvfile))
        headers = list(STRdb[0])

    # Opening second CL argument containing DNA Sequence
    with open(argv[2], "r") as DNAtxt:

        # Reading contents of txt into list
        DNA = DNAtxt.read()

    # Function to find and print person
    print(findperson(DNA, STRdb))


def countSTR(DNA, STR):

    # List of indexes where STR occurs in DNA string
    indexlist = []

    # Variable to store length of DNA
    DNAlength = len(DNA)
    # Variable to store length of STR
    STRlength = len(STR)

    # Looping through DNA string
    for i in range(DNAlength):

        # Storing indices of STR in the list
        index = DNA.find(STR, i)
        if index == -1:
            break
        if index not in indexlist:
            indexlist.append(index)

    # Number of STRs in DNA sequence
    STRcount = len(indexlist)
    # Variable to store length of consecutive repeats of the STR in the DNA sequence
    temp = 1
    # Variable to store length of longest run of consecutive repeats of the STR in the DNA sequence
    maxcount = 1
    for i in range(STRcount-1):
        if (indexlist[i+1] - indexlist[i]) == STRlength:
            temp += 1
        else:
            temp = 1
        if temp > maxcount:
            maxcount = temp
    return maxcount


def findperson(DNA, Database):

    number = len(list(Database[0]))
    tempList = list(Database[0])

    # List of STRs
    STRlist = []
    for i in range(1, number):
        STRlist.append(tempList[i])

    strcount = len(STRlist)
    dblength = len(Database)

    # List of STR counts
    strcountlist = []
    for i in range(strcount):
        strcountlist.append(countSTR(DNA, STRlist[i]))

    foundname = True
    for i in range(dblength):
        foundname = True
        for k in range(strcount):
            if int(Database[i][STRlist[k]]) != int(strcountlist[k]):
                foundname = False
                break
        if foundname == True:
            return Database[i]['name']

    # If not no such person found, print no found
    return ("No Match")


main()
