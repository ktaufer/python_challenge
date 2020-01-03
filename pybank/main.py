import csv
import os

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    pandl = []
    totalmonths=0
    maxpl=0
    minpl=0
    for row in csvreader:
        totalmonths=totalmonths+1
        pandl.append(int(row[1]))
        if int(row[1])>int(maxpl):
            maxpl=row[1]
            bestmonth=row[0]
        elif int(row[1])<int(minpl):
            minpl=row[1]
            worstmonth=row[0]
    totalpandl=sum(pandl)
    avepl=(totalpandl/totalmonths)

print("_________________________________________________")
print("Financial Analysis")
print("_________________________________________________")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalpandl}")
print(f"Average Monthly Change: ${round(avepl)}")
print(f"Greatest Increase in Profits: {bestmonth} (${maxpl})")
print(f"Greatest Decrease in Profits: {worstmonth} (${minpl})")
print("_________________________________________________")




with open("Financial_Analysis.txt","w+") as output:
    print("_________________________________________________", file=output)
    print("Financial Analysis", file=output)
    print("_________________________________________________", file=output)
    print(f"Total Months: {totalmonths}", file=output)
    print(f"Total: ${totalpandl}", file=output)
    print(f"Average Monthly Change: ${round(avepl)}", file=output)
    print(f"Greatest Increase in Profits: {bestmonth} (${maxpl})", file=output)
    print(f"Greatest Decrease in Profits: {worstmonth} (${minpl})", file=output)
    print("_________________________________________________", file=output)


