import os
import csv 

delimiter = ','
quote_character = '"'

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
                
    csv_fp = open(DATAFILE, 'rb')
    csv_reader = csv.DictReader(csv_fp, fieldnames=[], restkey='undefined-fieldnames', delimiter=delimiter, quotechar=quote_character)
    
    current_row = 0
    for row in csv_reader:
        current_row += 1
        if current_row > 11:
            break
	# Use heading rows as field names for all other rows.
        if current_row == 1:
            csv_reader.fieldnames = row['undefined-fieldnames']
            continue

        print (csv_reader.fieldnames[0]+':',row['Title'],csv_reader.fieldnames[1]+':',row['Released'],csv_reader.fieldnames[2]+':',row['Label'],csv_reader.fieldnames[3]+':',row['UK Chart Position'],csv_reader.fieldnames[4]+':',row['US Chart Position'],csv_reader.fieldnames[5]+':',row['BPI Certification'],csv_reader.fieldnames[6]+':',row['RIAA Certification'])
        
    return data
