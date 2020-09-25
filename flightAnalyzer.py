import csv
import time

#['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'AIRLINE', 'FLIGHT_NUMBER', 'TAIL_NUMBER', 'ORIGIN_AIRPORT', 
#'DESTINATION_AIRPORT', 'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME', 'DEPARTURE_DELAY', 'TAXI_OUT', 'WHEELS_OFF', 
#'SCHEDULED_TIME', 'ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'WHEELS_ON', 'TAXI_IN', 'SCHEDULED_ARRIVAL', 
#'ARRIVAL_TIME', 'ARRIVAL_DELAY', 'DIVERTED', 'CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 
#'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']
numToMonth = ["January","February","March","April","May","June","July","August","September","October","November","December"]
numToDay = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def main():
    print('\nSince this is processing over 9 million flights in 2015 (according to https://www.bts.gov/newsroom/2015-us-based-airline-traffic-data), it is unrealistic to process and print every single flight for that year unless you don\'t mind waiting two hours for everything to show. This is why that option is not availible. With that said:\n')
    print('1) View top 20 busiest airports in a given month (busiest is defined as the combined number of planes flying both in and out of an airport)')
    print('2) View top 20 busiest airports on a given day (busiest is defined as the combined number of planes flying both in and out of an airport)')
    print('3) Show all flights by a particular aircraft in a given month (requires the tail number of the aircraft as input)')
    print('4) Return the top 5 airlines with least amount of delays in a month')
    print('5) Show longest flight time in a given month (flight time is defined as time spent in the air)')
    print('6) Show all flights on a given day and month\n')
    while True:
        #if the user gave a valid integer value between 1 and 7
        try:
            numberChosen = input()
        #catch invalid input
        except ValueError:
            print('Not a valid value. Try again:')
            continue
        else:
            if int(numberChosen) > 0 and int(numberChosen) < 8:
                rerouteOption(numberChosen)
                break

#executes a particular function based on what number the user chose
def rerouteOption(valueChosen):
    if int(valueChosen) == 1 : busiest_airports_in_month()
    elif int(valueChosen) == 2 : busiest_airports_in_day()
    elif int(valueChosen) == 3 : aircraft_flight_schedule()
    elif int(valueChosen) == 4 : airline_least_delays()
    elif int(valueChosen) == 5 : longest_flight_time_in_month()
    elif int(valueChosen) == 6 : show_flights_day_month()
    
def busiest_airports_in_month():
    #structure as follows:
    #  "airport","busyness/business (idk) value"
    #latter int is incremented if there is a flight where a plane is flying in/out of that airport

    list_busiest_airports = {}

    month = getMonth()

    #first half of the month
    with open("month"+str(month)+".csv") as file:
        reader = csv.reader(file)
   
        for row in reader:
            #if key does exist in dictionary
            #departures count towards how busy an airport is
            if row[7] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[7])
                list_busiest_airports[row[7]] = (value_at_key + 1)

            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[7] not in list_busiest_airports:
                list_busiest_airports[row[7]] = 1 

            #arrivals count towards how busy an airport is
            if row[8] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
                list_busiest_airports[row[8]] = (value_at_key + 1)
            
            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[8] not in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
    
                list_busiest_airports[row[8]] = 1
    #second half of the month
    with open("month"+str(month)+"_2.csv") as file:
        reader = csv.reader(file)
   
        for row in reader:
            #if key does exist in dictionary
            #departures count towards how busy an airport is
            if row[7] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[7])
                list_busiest_airports[row[7]] = (value_at_key + 1)

            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[7] not in list_busiest_airports:
                list_busiest_airports[row[7]] = 1 

            #arrivals count towards how busy an airport is
            if row[8] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
                list_busiest_airports[row[8]] = (value_at_key + 1)
            
            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[8] not in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
                list_busiest_airports[row[8]] = 1

    #sort airports in descending order (the most busy come first)
    sort_airports = sorted(list_busiest_airports.items(), key=lambda x:x[1],reverse=True)
    trackInt = 0
    print("Top 20 busiest airports in " + numToMonth[month - 1])
    for i in sort_airports:
        if trackInt < 20:
            print(str(trackInt + 1)+ ". " + i[0])
            trackInt += 1
        else:
            break





def busiest_airports_in_day():
    month = getMonth()
    day = getDay()

    #csv files are split up for convenience, which means that we are opening different csv files
    #based on the month and day (if day > 15, open _2 csv file. else open regular)
    #this will make it easier and quicker to look for a particular day
    open_file_name = "month" + str(month) + ('_2.csv' if day > 15 else '.csv')
    
    list_busiest_airports = {}

    with open(open_file_name) as file:
        reader = csv.reader(file)
   
        for row in reader:
            #if key does exist in dictionary
            #departures count towards how busy an airport is
            if row[7] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[7])
                list_busiest_airports[row[7]] = (value_at_key + 1)

            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[7] not in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[7])
                list_busiest_airports[row[7]] = 1 

            #arrivals count towards how busy an airport is
            if row[8] in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
                list_busiest_airports[row[8]] = (value_at_key + 1)
            
            #if value does not exist in dictionary
            #1 because if we are inserting it, we know that there is at least 1 incoming/outgoing flight
            elif row[8] not in list_busiest_airports:
                value_at_key = list_busiest_airports.get(row[8])
                list_busiest_airports[row[8]] = 1

    #sort airports in descending order (the most busy come first)
    sort_airports = sorted(list_busiest_airports.items(), key=lambda x:x[1],reverse=True)
    trackInt = 0
    print("Top 20 busiest airports on " + numToMonth[month - 1] + " " + str(day))
    for i in sort_airports:
        if trackInt < 20:
            print(str(trackInt + 1)+ ". " + i[0])
            trackInt += 1
        else:
            break





    
#requires tail number
def aircraft_flight_schedule():
    tail_number = input("Enter an aircraft's tail number: ")
    month = getMonth()

    open_file_name = "month" + str(month) + ".csv"

    #first half of the month
    with open(open_file_name) as file:
        reader = csv.reader(file)
   
        for row in reader:
            if str(tail_number).strip() == row[6] and row[1] == str(month):
                print(cleanup_row_text(row))
    
    #second half of the month
    with open("month" + str(month) + "_2.csv") as file:
        reader = csv.reader(file)
   
        for row in reader:
            if str(tail_number).strip() == row[6] and row[1] == str(month):
                print(cleanup_row_text(row))

    

# there are two columns in the csv for delays: departure delay and arrival delay
# if an airline departs late but still arrives on time, it is viewed/recorded as being on time, right?
# (this is almost never the case since departure delays impact the rest of the trip duration (not to mention bad weather, wind, air traffic sometimes))
# this function counts arrival delays as general delays because departure delay doesn't matter
def airline_least_delays():
    #it is a list that contains:
    #airline name
    #int of how many delays it has had
    
    list_airline_delays = {}

    month = getMonth()

    #first half of the month
    with open("month"+str(month)+".csv") as file:
        reader = csv.reader(file)

        for row in reader:
            #if key does exist in dictionary AND the airline was late, it is recorded
            #i defined late as an arrival delay of over 5 minutes (can easily be adjusted obv)
            if row[22] in list_airline_delays and int(row[22]) > 5:
                value_at_key = list_airline_delays.get(row[22])
                list_airline_delays[row[4]] = (value_at_key + 1)

            #if value does not exist in dictionary
            elif row[7] not in list_airline_delays:
                value_at_key = list_airline_delays.get(row[22])
                list_airline_delays[row[4]] = 1
        
    #second half of the month
    with open("month"+str(month)+"_2.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            #if key does exist in dictionary AND the airline was late, it is recorded
            #i defined late as an arrival delay of over 5 minutes (can easily be adjusted obv)
            if row[22] in list_airline_delays and int(row[22]) > 5:
                value_at_key = list_airline_delays.get(row[22])
                list_airline_delays[row[4]] = (value_at_key + 1)

            #if value does not exist in dictionary
            elif row[7] not in list_airline_delays:
                value_at_key = list_airline_delays.get(row[22])
                list_airline_delays[row[4]] = 1





    
    list_airline_delays = sorted(list_airline_delays.items(), key=lambda x:x[1],reverse=True)
    trackInt = 0

    print("Airlines with least amount of delays in " + numToMonth[month - 1] + ": ")
    for i in list_airline_delays:
        if trackInt < 5:
            print(str(trackInt + 1)+ ". " + i[0])
            trackInt += 1

def longest_flight_time_in_month():
    month = getMonth()
    open_file_name = "month" + str(month) + ".csv"
    longest_time = 0
    flight = ""

    with open(open_file_name) as file:
        reader = csv.reader(file)
   
        for row in reader:            
            #if the flight happened (was not cancelled)
            if row[16]:
                if int(row[16]) > longest_time and row[1] == str(month):
                    longest_time = int(row[16])
                    flight = row

    with open("month" + str(month) + "_2.csv") as file:
        reader = csv.reader(file)
   
        for row in reader:            
            #if the flight happened (was not cancelled)
            if row[16]:
                if int(row[16]) > longest_time and row[1] == str(month):
                    longest_time = int(row[16])
                    flight = row

        
    print("Longest flight time was: " + cleanup_row_text(flight))




#we will find all flights on a particular day in a particular month
def show_flights_day_month():
    month = getMonth()
    day = getDay()

    #csv files are split up for convenience, which means that we are opening different csv files
    #based on the month and day (if day > 15, open _2 csv file. else open regular)
    #this will make it easier and quicker to look for a particular day
    open_file_name = "month" + str(month) + ('_2.csv' if day > 15 else '.csv')
    
    with open(open_file_name) as file:
        reader = csv.reader(file)
   
        for row in reader:
            #if the row we are looking at matches the day we entered, print the result
            if row[2] == str(day) and row[1] == str(month):
                print(cleanup_row_text(row))
                
    
    


#cleans up the row format in the csv [YEAR,MONTH,DAY,ETC] to look nicer
#takes in a row as argument, returns newly formatted row
#DAY_OF_WEEK (full), MONTH DAY: AIRLINE FLIGHT_NUMBER "from" ORIGIN_AIRPORT to DESTINATION_AIRPORT. "Departed at" DEPARTURE_TIME "and arrived at" ARRIVAL_TIME. "Total flight time: " ELAPSED_TIME. "Distance:" DISTANCE
def cleanup_row_text(row):
    raw_departure_time = row[10]
    formatted_depature_time = raw_departure_time[:2] + ":" + raw_departure_time[2:]
    raw_arrival = row[21]
    formatted_arrival = raw_arrival[:2] + ":" + raw_arrival[2:]
    formatted_flight_time = 0
    finalStatement = ""
    day_info = numToDay[int(row[3]) - 1] + ", " + numToMonth[int(row[1]) - 1] + " " + row[2] + ": "
    origin_to_destination = " from " + row[7] + " to " + row[8] + ". "

    #if there is a value for flight time, flight happened
    #if not, it was cancelled
    if row[15]:
        raw_flight_time = int(row[15])/60
        formatted_flight_time = str(round(raw_flight_time,2))

    #if flight happened
    if row[15]:

        flight_number = row[4] + row[5]
        departure_arrival_times = "Departed at " + formatted_depature_time + " and arrived at " + formatted_arrival + ". "

        flight_info = "Total flight time: " + formatted_flight_time + " hours. "
        distance = "Distance flown: " + row[17] + " miles"
        
        finalStatement = day_info + flight_number + origin_to_destination + departure_arrival_times + flight_info + distance
    
    else:
        finalStatement = day_info + row[4] + row[5] + origin_to_destination + "FLIGHT WAS CANCELLED"
    return finalStatement



#returns a month in numerical format (easier to analyze in file)
#user can enter month in string format ("November") or number (11)
def getMonth():
    #we want analyze month to be a number that corresponds to a month
    while True:
        analyzeMonth = input('Enter the month you want to analyze (number from 1-12 or the month itself): ')

        #if user entered string
        if(analyzeMonth.strip() in numToMonth):
            month = numToMonth.index(analyzeMonth.strip()) + 1 # + 1 gets the real month from numToMonth
            return month
            break
        #if user entered number (testing that it is a valid number)
        else:
            try:
                if(int(analyzeMonth) >= 1 and int(analyzeMonth) <= 12):
                    month = int(analyzeMonth)
                    return month
                    break
                else:
                    print("Out of range")
            except ValueError:
                print('Not a valid value')

def getDay():
    while True:
        analyzeDay = input('Enter the day you want to analyze: ')

        try:
            if(int(analyzeDay) >= 1 and int(analyzeDay) <= 31):
                day = int(analyzeDay)
                return day
                break
            else:
                print("Out of range")
        except ValueError:
                print('Not a valid value')













if __name__ == "__main__":
    main()