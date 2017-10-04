import os
import csv

directory = "features/deviceMotion_walking_rest"

counter = 0

for filename in os.listdir(directory):
    
    filename = directory + "/" + filename
    print(filename)
    walk = open(filename, 'r')
    lst = csv.reader(walk, delimiter=',')
    lines1 = list(lst)
    walk.close()
    newlines = []
    walk = open("merged.csv", 'r')
    lst = csv.reader(walk, delimiter=',')
    lines = list(lst)
    walk.close()
    #print(lines)
    firstline = 0
    if( len(lines) != len(lines1) and counter != 0):
        print(len(lines), len(lines1))
        break
    for i in range(len(lines1)):
        if counter != 0: 
            line = ','.join(lines[i])
        line1 = ','.join(lines1[i]) 
        #print(line)
        #print(line1)
        newline = ""
        if( firstline == 0 ):
            print("hello")
            if (counter == 0): #first file: put Id,Medpoint,<First feature name>
                newline = "Id,Medpoint," + filename.split("/")[-1].split(".")[0]
            else:
                newline = line.strip("\n") + "," + filename.split("/")[-1].split(".")[0]
            firstline = 1
        else:
            if (counter == 0):
                newline = line1.strip("\n")
            else:
                newline = line.strip("\n") + "," + line1.strip("\n").split(",")[-1]
        #print(newline)
        newlines.append(newline)
    counter = 1

    #print('\n'.join(newlines))
    walk_w = open("merged.csv", 'w')
    #writer = csv.writer(walk_w)
    for line in newlines:
        #writer.writerow([line])
        walk_w.write(line + "\n")
    walk_w.close()
