import os
import csv



#currentdirpath = os.getcwd()
#filename = 'crewTimeMorgand.csv'
#file_path = os.path.join(os.getcwd(), filename)

def get_file_path(filename):
    #currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    print(file_path)
    return file_path



path = get_file_path('crewTimeMorgand.csv')


def read_csv(file_path):
    uniqueId = {}
    i = 0
    with open(file_path, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not "Name" in row:
                my_Name = row[0]
                #my_name = row[0].split('a')
                i += 1
                uniqueId[i] = my_Name
    print (uniqueId)


read_csv(path)
