Python Flight Analyzer (from all domestic flights in 2015)

flightAnalyzer.py is a flight analyzer script, which returns certain information about domestic flights in the United States in 2015. The user has the following options:

1) View top 20 busiest airports in a given month (busiest is defined as the combined number of planes flying both in and out of an airport)
2) View top 20 busiest airports on a given day (busiest is defined as the combined number of planes flying both in and out of an airport)
3) Show all flights by a particular aircraft in a given month (requires the tail number of the aircraft as input)
4) Return the top 5 airlines with least amount of delays in a month
5) Show longest flight time in a given month (flight time is defined as time spent in the air)
6) Show all flights on a given day and month

The CSV file of ALL domestic flights in 2015 was taken from https://www.kaggle.com/usdot/flight-delays?select=flights.csv

Since it would have taken around an hour to search and find information in the CSV given by kaggle, I split it up using the provided csvSplitter.py. This CSV splitter script was specifically coded for this project, but it can be easily adjusted to accomodate for all CSV types.

The CSVs are split up by half months. This means that a file without a "_2" refers to the first half of a month (days 1-15). A file with a "_2" refers to the second half of a month (16-end of month). Splitting up the CSVs in this way allowed for extremely fast retrieval of flight information, no matter the day/month input. If I had left the original CSV with around 9m+ entries, it would have taken an hour or more to fetch a simple piece of information (I know this because the splitter script took around 1.5 hours to run)

Usage Information:
- Make sure the latest version of Python is installed
    
- Open up command prompt and navigate to the folder where the flightAnalyzer.py script and CSV files are located
    
- Execute the python script
    
- Follow instructions
