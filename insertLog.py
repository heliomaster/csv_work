import sys
import os
import csv
import datetime

# def main():
if len(sys.argv) != 2:
    print ("usage: {} <logbook-file>").format(sys.argv[0])
    sys.exit(1)


filename = sys.argv[1]
file_exits = os.path.isfile(filename)


with open(filename, 'a') as target_file:
    fieldnames = ['date', 'actype', 'tail', 'apfrom', 'apto']
    writer = csv.DictWriter(target_file, fieldnames=fieldnames)
    if not file_exits:
        writer.writeheader()
    date = input("Enter date in YYYY-MM-DD: ")
    year, month, day = map(int, date.split('-'))
    date1 = datetime.date(year, month, day)
    actype = input("Enter A/C type: ")
    tail = input("Tail Number: ")
    apfrom = input("Departure Airport: ")
    apto = input("Arrival airport: ")
    newL = '\n'
    #blockhours = input(int("block Hours: "))
    log_entry = ','.join((str(date1), actype, tail, apfrom, apto, newL))
    #block_combine=datetime.combine(date1, blockhours)

    target_file.write(log_entry)


# if __name__=='__main__':
#    main(test.csv)
