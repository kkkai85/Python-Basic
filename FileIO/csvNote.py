import csv

fp = open("csvNote_read.csv")
r = csv.reader(fp)
for row in r:
    print(row)

data = [("one", 1, 2.5), ("two", 42.3, 11)]
with open("csvNote_out.csv", "w") as fc:
    w = csv.writer(fc)
    w.writerows(data)