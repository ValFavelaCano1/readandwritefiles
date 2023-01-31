import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

sales = csv.reader(infile, delimiter=",")

next(sales)

outfile.write("Customer | Total\n")

customer_id = 250
total_sales = 0

for row in sales:
    if int(row[0]) == customer_id:
        total_sales += float(row[3]) + float(row[4]) + float(row[5])
    else:
        if customer_id != 249:
            outfile.write(
                str(format(customer_id, "9"))
                + " "
                + format(total_sales, ">10.2f")
                + "\n"
            )
        customer_id = int(row[0])
        total_sales = float(row[3]) + float(row[4]) + float(row[5])
outfile.write(
    str(format(customer_id, "9")) + " " + format(total_sales, ">10.2f") + "\n"
)

outfile.close()
