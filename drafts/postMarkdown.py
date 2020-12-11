import sys
import os
import re

def getSmall(read_file, write_file):

    
    with open(read_file, "r") as rf:
        with open(write_file, "w+") as wf:
                if rf.mode == "r":
                    # Get all the lines from the document
                    lines = rf.readlines()
                    count = 1
                    # Look through a single line of the document
                    for x in lines:
                        startIndex = 0
                        endIndex = 0
                        # Continues to search through the line until it finds all the instances of "<small>"
                        while startIndex < len(x):
                            startIndex = x.find("<small>", startIndex)
                            if startIndex == -1:
                                break
                            endIndex = x.find("</small>", startIndex)
                            inside = x[startIndex + 7:endIndex]
                            # Writes the footnote to an output file in the correct format
                            wf.write("[^" + str(count) + "]: " + inside + "\n")
                            count += 1
                            startIndex = endIndex + 8
                        
    rf.close()
    wf.close()


def writeFootnote(read_file, write_file):

    
    with open(read_file, "r") as rf:
        with open(write_file, "w+") as wf:
                if rf.mode == "r":
                    # Get all the lines from the document
                    lines = rf.readlines()
                    count = 1
                    # Look through a single line of the document
                    for x in lines:
                        index = 0
                        # Continues to search through the line until it finds all the instances of "<small>"
                        while index < len(x):
                            temp = index
                            index = x.find("</small>", index)
                            if index == -1:
                                wf.write(x[temp:])
                                break                        
                            # Writes the line (with the added footnote) to another file
                            index += 8
                            wf.write(x[temp:index] + "[^" + str(count) + "]")
                            count += 1
                wf.write("\n\n")
    rf.close()
    wf.close()



def getHeaders(read_file):

    with open(read_file, "r") as rf:
        with open("temp.txt", "w+") as wf:

            if rf.mode == "r":
                lines = rf.readlines()

                wf.write("\n")
                for x in lines:
                    if(x[0:3] == "## "):
                        wf.write("- " + x[3:])
                    if(x[0:4] == "### "):
                        wf.write("\t- " + x[4:])
                    if(x[0:5] == "#### "):
                        wf.write("\t\t- " + x[5:])
                    if(x[0:6] == "##### "):
                        wf.write("\t\t\t- " + x[6:])
                wf.write("\n")
            
    rf.close()
    wf.close()

    with open(read_file, "r") as rf:
        with open("temp.txt", "r") as wf:
            with open("temp1.txt","w+") as ff:
                if rf.mode == "r":
                    if wf.mode == "r":
                        linesMain = rf.readlines()
                        linesHeaders = wf.readlines()
                        count = 0
                        numLines = 0

                        for x in linesMain:
                            ff.write(x)
                            numLines += 1
                            if(x[0:3] == "---"):
                                    count += 1
                            if(count == 2):
                                break
                        
                        for y in linesHeaders:
                            ff.write(y)

                        count = -1
                        for z in linesMain:
                            count += 1
                            if(count > numLines):
                                print(z)
                                print(numLines)
                                ff.write(z)
                        
    rf.close()
    wf.close()
    ff.close()

    os.remove("temp.txt")
    writeFootnote("temp1.txt", "temp2.txt")
    getSmall("temp1.txt", "temp3.txt")

    filenames = ["temp2.txt", "temp3.txt"]
    with open("postMarkdown.md", "w+") as outfile:
        for file in filenames:
            with open(file) as infile:
                outfile.write(infile.read())

    os.remove("temp1.txt")
    os.remove("temp2.txt")
    os.remove("temp3.txt")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 1 command line argument")
    
    read_file = sys.argv[1]
    getHeaders(read_file)