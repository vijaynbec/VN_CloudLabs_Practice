import csv
csv_inputfile = "read_csv.csv"

# get all CSV comma seperated records into string value with header
with open(csv_inputfile) as csv_read:
    reader = csv.reader(csv_read)
    for row in reader:
        print(row)