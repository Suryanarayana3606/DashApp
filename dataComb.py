import csv
import os

dataFile = "./data"
finalFile = "./finalData.csv"

with open(finalFile, "w", newline='') as f:
    writer = csv.writer(f)

    title = ["sales", "date", "region"]
    writer.writerow(title)

    for file in os.listdir(dataFile):
        with open(f'./{dataFile}/{file}', "r") as fr:
            reader = csv.reader(fr)
            count=0
            for row in reader:
                if count>0:
                    product = row[0]
                    price = row[1]
                    quantity = row[2]
                    date = row[3]
                    region = row[4]

                    if product == "pink morsel":
                        price = float(price[1:])
                        sales = int(quantity)*price

                        newRow = [sales, date, region]
                        writer.writerow(newRow)
                count+=1