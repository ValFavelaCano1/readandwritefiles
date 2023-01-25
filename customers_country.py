import csv

infile = open("customers.csv", "r")
outfile = open("customers_country.csv", "w")

customers = csv.reader(infile, delimiter=",")

outfile.write("First Name, Last Name, Country\n")

for row in customers:
    first_name = row[1]
    last_name = row[2]
    country = row[4]
    outfile.write(first_name + "," + last_name + "," + country + "\n")

outfile.close()
