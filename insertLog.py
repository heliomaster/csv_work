import sys
import os
import csv
import datetime


'''Opens and writes a csv file with filename.csv as argument in terminal
usage: python3 insertLog.py test.csv'''


# check user provided arguments if not print message and exit
if len(sys.argv) != 2:
    print ("usage: {} <logbook-file>").format(sys.argv[0])
    sys.exit(1)

# sys.argv[1] contains first argument ie file
filename = sys.argv[1]
file_exists = os.path.isfile(filename)


with open(filename, 'a', newline='') as target_file:
    fieldnames = ['date', 'actype', 'tail', 'apfrom', 'apto', 'blockhours', ]
    writer = csv.DictWriter(target_file, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()

    while True:

        date = input("Enter date in YYYY-MM-DD: ")
        if date == 'stop':
            break
        else:
            year, month, day = map(int, date.split('-'))
            date1 = datetime.date(year, month, day)
            blockhours = input("block Hours: ")
            actype = input("Enter A/C type: ")
            tail = input("Tail Number: ")
            apfrom = input("Departure Airport: ")
            while(len(apfrom)) > 4:
                print("Error! Only 4 ICAO letters allowed!")
                apfrom = input("Departure Airport: ")
            apto = input("Arrival airport: ")
            while(len(apfrom)) > 4:
                print("Error! Only 4 ICAO letters allowed!")
                apto = input("Arrival airport: ")
            newL = '\n'

            log_entry = ','.join(
                (str(date1), actype, tail, apfrom, apto, blockhours, newL))
            #block_combine=datetime.combine(date1, blockhours)

            # write log_entry to taget file
            target_file.write(log_entry)


# if __name__=='__main__':
#    main(filename)
