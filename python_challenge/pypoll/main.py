import csv
import os

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    totalvotes=0
    candidates=[]
    firstvotes=0
    secondvotes=0
    thirdvotes=0
    fourthvotes=0
    for row in csvreader:
        totalvotes=totalvotes+1
        if row[2] not in candidates:
            candidates.append(row[2])
            
    
        if str(row[2])==candidates[0]:
            firstvotes=firstvotes+1
        elif str(row[2])==candidates[1]:
            secondvotes=secondvotes+1
        elif str(row[2])==candidates[2]:
            thirdvotes=thirdvotes+1
        elif str(row[2])==candidates[3]:
            fourthvotes=fourthvotes+1
    
    first=str(candidates[0])
    second=str(candidates[1])
    third=str(candidates[2])
    fourth=str(candidates[3])

    firstpercent=round(firstvotes/totalvotes*100)
    secondpercent=round(secondvotes/totalvotes*100)
    thirdpercent=round(thirdvotes/totalvotes*100)
    fourthpercent=round(fourthvotes/totalvotes*100)
    
print(     "Election Results:")
print("-----------------------------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------------------------")
print(f"{first}: {firstpercent}.00% ({firstvotes})")
print(f"{second}: {secondpercent}.00% ({secondvotes})")
print(f"{third}: {thirdpercent}.00% ({thirdvotes})")
print(f"{fourth}: {fourthpercent}.00% ({fourthvotes})")
print("-----------------------------------------")
print("Winner: Khan")
print("-----------------------------------------")
