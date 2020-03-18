#A. The total number of months included in the dataset
#B. The net total amount of "Profit/Losses" over the entire period
#C. The average of the changes in "Profit/Losses" over the entire period
#D. The greatest increase in profits (date and amount) over the entire period
#E. The greatest decrease in losses (date and amount) over the entire period

#import dependencies
import csv
import os

#variables and lists
mon_count = 0
dates = []
total_rev = 0
total_rev_diff = 0
revs = []
mon_diff = []
total_mon_diff = 0
avg_mon_change = 0

# Create the path (os (specific path))
csvpath = os.path.join('Raw_Data','budget_data.csv')

#read csv file
with open(csvpath, newline='') as budget_file:
    reader = csv.reader(budget_file, delimiter=',')
    csv_header = next(reader)
    for line in reader:
#A
    #count number of months
        mon_count += 1   
    #list of dates 
        dates.append(line[0])
    #list of revenues
        revs.append(float(line[1]))
#B
    #total of revenues
        total_rev += float(line[1])    
    #interate through list of rev (-except last calc)
    for i in range(len(revs)-1):
        #mon_diff is a list of rev diff btwn each month
        mon_diff.append(revs[i+1]- revs[i])
    #calc total change of all months
        total_mon_diff = total_mon_diff + mon_diff[i]
#C
    #calc avg change
        avg_mon_change = total_mon_diff / len(mon_diff)
        avg_mon_ch2 = int(avg_mon_change)
#D & E         
        if mon_diff[i]>= int(g_inc):
            ig_inc = mon_diff[i]
            g_inc_date = dates[i+1]
        elif mon_diff[i]<= int(g_dec):
            g_dec = mon_diff[i]
            g_dec_date = dates[i+1]

#printed financial_summary            
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(mon_count))
print('Total: $' + str(total_rev) )
print('Average Change: $' + str(avg_mon_ch2))
print('Greatest Increase in Profits: '+ str(g_inc_date) +'  '+' ($'+str(int(g_inc))+')')
print('Greatest Decrease in Profits: '+ str(g_dec_date) +'  '+' ($'+ str(int(g_dec))+')')

#output financial summary
output_path = os.path.join('Raw_Data','financial_summary.txt')
with open(output_path,"w") as fh:
    fh.write('Financial Analysis\n')
    fh.write('----------------------------\n')
    fh.write('Total Months: ' + str(mon_count)+ '\n')
    fh.write('Total: $' + str(total_rev)+ '\n')
    fh.write('Average Change: $' + str(avg_mon_ch2)+ '\n')
    fh.write('Greatest Increase in Profits: '+ str(g_inc_date) +'  '+' ($'+str(int(g_inc))+')\n')
    fh.write('Greatest Decrease in Profits: '+ str(g_dec_date) +'  '+' ($'+ str(int(g_dec))+')')
