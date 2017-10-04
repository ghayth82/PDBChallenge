import os
import csv

directory = "Train_features/deviceMotion_walking_rest_new/"

counter = 1
for filename in os.listdir(directory):
    print(filename)
    filename = directory + "/" + filename
    dictionary = {}
    with open(filename) as f:
            for line in f:
                line = line.strip("\n").split(",")
                dictionary[line[0]] = line[1]
                #print(line)
    #print(dictionary.keys())
    newlines = []
    walk = open("Walking Activity Training (copy).csv", 'r')
    lines = csv.reader(walk, delimiter=',')
    #print(lines)
    firstline = 0
    for line in lines:
        line = ','.join(line)
        test = line.strip("\n").split(",")
        #print(line)
        newline = ""
        if( counter == 0 ):
            if( firstline == 0 ):
                newline = test[2] + "," + filename.split("/")[-1].split(".")[0]
                firstline = 1
            else:
                #print(test)
                #print(test[2])
                if(test[2] in dictionary.keys()):
                    #print("Hello")
                    newline = test[2] + "," + dictionary[test[2]]
                else:
                    newline = test[2] + ",0"
            #print(newline)
            newlines.append(newline)
        else:
            if( firstline == 0 ):
                newline = line + "," + filename.split("/")[-1].split(".")[0]
                firstline = 1
            else:
                #print(test)
                #print(test[2])
                if(test[0] in dictionary.keys()):
                    #print("Hello")
                    newline = line + "," + dictionary[test[0]]
                else:
                    newline = line + ",0"
            #print(newline)
            newlines.append(newline)
    counter+=1
    walk.close()

    #print('\n'.join(newlines))
    walk_w = open("Walking Activity Training (copy).csv", 'w')
    #writer = csv.writer(walk_w)
    for line in newlines:
        #writer.writerow([line])
        walk_w.write(line + "\n")
    walk_w.close()
