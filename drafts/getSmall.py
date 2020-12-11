import sys
import re

def getSmall(read_file, write_file):

    # tf = open("temp_file", "x")
    
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
                            # Writes the footnote to an outpute file in the correct format
                            wf.write("[^" + str(count) + "]: " + inside + "\n")
                            count += 1
                            startIndex = endIndex + 8
                        
    rf.close()
    wf.close()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 2 command line arguments")
    
    read_file = sys.argv[1]
    write_file = sys.argv[2]
    getSmall(read_file, write_file)