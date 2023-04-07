
def count_lines_within_file(file):
    line_count = 0
    lines = file.readlines()
    listLength = len(lines) -1 
    net_total = 0
    first_number =0 
    last_number=0
    greatest_increase = 0
    greatest_decrease =0
    previous_month = 0
    allLines = enumerate(lines)
    month_increase =0
    month_decrease = 0
    
    
    for i, line in allLines:
        if i == 0:
            continue # Skip the first line
        else:
            # Do something with the line
            line_count = line_count +1
            data = line.strip().split(",")
            net_total = net_total + int(data[1])
            if i == 1 :
                first_number = int(data[1])
                previous_month = int(data[1])
                continue

            if listLength == line_count:
                last_number = int(data[1])

            profit = int(data[1]) - previous_month 

            if profit < greatest_decrease:
                greatest_decrease = profit
                month_decrease = data[0]

            if profit > greatest_increase:
                greatest_increase = profit
                month_increase = data[0]

            previous_month = int(data[1])
            
            #print(data)

    average_change= (last_number-first_number) / (line_count -1)

    print("Total months: " + str(line_count))
    print("Net Total: $" + str(net_total))
    print("Average Change: $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: " + month_increase+" ($" + str(greatest_increase) +")")
    print("Greatest Decrease in Profits: " + month_decrease+" ($" + str(greatest_decrease) +")")
    
    
file = 'Resources/budget_data.csv'

with open(file, 'r') as text:

    count_lines_within_file(text)

    lines = text.read()

    





    



   
