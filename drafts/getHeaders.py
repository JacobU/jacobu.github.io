import sys
import os

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

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 1 command line argument")
    
    read_file = sys.argv[1]
    getHeaders(read_file)