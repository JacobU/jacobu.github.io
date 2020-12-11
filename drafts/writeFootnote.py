import sys
import re

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


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 2 command line arguments")
    
    read_file = sys.argv[1]
    write_file = sys.argv[2]
    writeFootnote(read_file, write_file)