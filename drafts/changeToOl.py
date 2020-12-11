import sys

def changeToOl(read_file):

    # tf = open("temp_file", "x")
    
    with open(read_file, "r") as rf:
        with open("olHeaders.txt", "w+") as wf:
                if rf.mode == "r":
                    # Get all the lines from the document
                    lines = rf.readlines()
                    # Look through a single line of the document
                    wf.write("\n<div class='toc'>\n")
                    for x in lines:
                        x = x.replace("<ul>","<ol>")
                        x = x.replace("</ul>", "</ol>")
                        wf.write(x)
                    wf.write("</div>\n\n")
    rf.close()
    wf.close()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("You've entered the wrong number of command line arguments. This script takes 1 command line arguments")
    
    read_file = sys.argv[1]
    changeToOl(read_file)