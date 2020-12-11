import sys
import os

def placeHeaders(read_file, header_file):

    with open(read_file, "r") as rf:
        with open(header_file, "r") as wf:
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
                                ff.write(z)
                        
    rf.close()
    wf.close()
    ff.close()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 2 command line argument")
    
    read_file = sys.argv[1]
    header_file = sys.argv[2]
    placeHeaders(read_file, header_file)