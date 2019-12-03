import os
import csv


filepath = os.path.join('Resources', 'budget_data.csv')
with open(filepath, newline = 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

budget = {}

total_months = []
net_total = []
greatest_increase = []
greatest_decrease = []

def print_data(budget_data):
    total_months = int(budget_data.csv[0])
    net_total = int(budget_data.csv[1])

    total_months = 0
    net_total = 0

    for row in budget_data:
        total_months += 1
        if row[2] in budget.keys():
            budget[row[2]] = budget[row[2]] + 1
        else:
            budget[row[2]] = 1
    
    for net_total in budget_data:
        net_total = net_total + 1

def average(budget_data):
    length = len(budget_data)
    Total = 0.0
    for net_total in net_total:
        total += net_total
    return Total / length

for greatest_increase in budget:
    greatest_increase  = net_total > 0

for greatest_decrease in budget:
    greatest_decrease = net_total < 0








    
    


