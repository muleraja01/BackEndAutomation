import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    names=[]
    stats=[]
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
print(names)
print(stats)
Index=names.index('sam')
loanStatus=stats[Index]
print('The loan Status is :'+loanStatus)


with open('utilities/loanapp.csv','a') as wFile:
    write=csv.writer(wFile)
    write.writerow(["Bob","Rejected"])
