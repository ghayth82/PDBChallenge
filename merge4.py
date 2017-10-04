import os
import csv

directory = "./Train_features/deviceMotion_walking_rest/"
directory_out = "./Train_features/deviceMotion_walking_rest_new/"

dict_map = {}
f = open("Walking Activity Training.csv", 'r')
lines = csv.reader(f, delimiter=',')
counter = 0
for line in lines:
    if counter == 0:
        counter = 1
    else:
        line = ','.join(line)
        test = line.strip("\n").split(",")
        if test[15] != '':
            dict_map[test[15]] = test[2]
f.close()

#print( '**', list(dict_map.keys())[0] )

counter = 1
for filename in os.listdir(directory):
    old_filename = filename
    #print(filename)
    filename = directory + "/" + filename
    dictionary = {} #id:value
    with open(filename) as f:
        for line in f:
            line = line.strip("\n").split(",")
            dictionary[line[0]] = line[-1]
            #print(line)
    #print( '$$', list(dictionary.keys())[0] )
    #break
    #newlines = []

    new_file = directory_out + old_filename
    f = open(new_file,'w')
    for id_, value in dictionary.items():
        if id_ in dict_map.keys():
            f.write(str(dict_map[id_]) + "," + str(value) + "\n")
    f.close()
    '''
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

                #test[0] is recordId
                #print(test[0])
                #dict_map_recordId_id
                if dict_map_recordId_id[test[0]] == '':
                    print("yay")
                    newline = line + ",0"
                elif dict_map_recordId_id[test[0]] in dictionary.keys():
                    print("Hello")
                    newline = line + "," + dictionary[dict_map_recordId_id[test[0]]]
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
    '''
