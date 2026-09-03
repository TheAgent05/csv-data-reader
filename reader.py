import csv


data = []
with open('somedata.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            row["amount"] = int(row["amount"])
        except ValueError:
            print("VALUE ERROR! USE ONLY NUMBER IN AMOUNT")
            print(f"Reason: {row}")
            continue
        data.append(row)


def getMaxSpending():
    maxExpense = None;
    item = None;
    for x in data:
        currAmount = x["amount"]
        if maxExpense != None:
            if currAmount > maxExpense:
                maxExpense = currAmount
                item = x
        else:
            maxExpense = currAmount
            item = x
    return item

def getTotalAmount():
    total = 0;

    for value in data:
        total += value["amount"]
    return total

def calculateTotals():
    categories = {}

    for value in data :
        category = value["category"]
        amount = value["amount"]
        if categories.get(category):
            categories[category] += amount
        else: 
            categories[category] = amount
            
    return sorted(categories.items(), key=lambda x: x[1], reverse=True)



def report():
    mostSpend = getMaxSpending()
    

    report = "====== Report ======\n"
    report += f"Total: ${getTotalAmount()} \n\n"
    report += "Categories:\n"

    for x in calculateTotals():
        report += f"  {x[0]} — ${x[1]}\n"

    report += "The biggest purchase:\n"
    report += f"  ${mostSpend['amount']} — {mostSpend['description']} ({mostSpend['category']}, {mostSpend['date']})\n\n"
    report += "============================="
    print(report)


report()
    

