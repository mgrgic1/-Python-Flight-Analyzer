#this file will split gigantic csv files (namely flights.csv) in order to make them more manageable
#manageable meaning: we can open/access them quicker (since the files are split up into smaller parts) and...
#...retrieving information faster through code because we are not going through the entire file, but rather segments of it

import csv
   
with open('flights.csv') as file:
    reader = csv.reader(file)
    onMonth = 1
   
    for row in reader:
        if row[1] == 'MONTH':
            continue
        
        else:
            #splits if the MONTHS are different
            #will automatically be handled below since we are changing the onMonth value
            if str(onMonth) != str(row[1]) and str(row[1]):
                #split
                print("---------------------SPLIT---------------------")
                onMonth = row[1]

            #prints out the first half of the month (days 1-15)
            if int(row[2]) <= 15:
                with open('month' + str(onMonth)+'.csv','a',newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row)
                    print('writing to ' + str(onMonth)+ '.csv')
            
            #splits if DAYS is greater than 15
            elif int(row[2]) > 15:
                with open('month' + str(onMonth)+'_2.csv','a',newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(row)
                    print('writing to ' + str(onMonth)+'_2'+ '.csv')

            

            
            