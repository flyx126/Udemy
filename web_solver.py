#We want the title, price, subscribers, reviews, percent of reviews, length
import csv
import os

title=[]               #Create the lists for each of the information required
price = []
subscribers = []
reviews = []
reviews_percent=[]
length=[]

#udemy_csv = "./Resources/web_starter.csv" relative file positions ./xxxxx/xxxx

udemy_csv = os.path.join(".","Resources","web_starter.csv") #instead of giving the whole adress of the file using the OS import

with open(udemy_csv,"r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") #reads the csv file and identifies each element separated by a coma
    for row in csvreader:                  #iterate in each row of the csv file
        title.append(row[1])              #selecting the 2nd element separated by a coma of each row of the csv file that is the title
        price.append(row[4])                #Selecting the 4th element of each row of the csv file that is the price
        subscribers.append(row[5])
        reviews.append(row[6])
        percent = round(int(row[6])/int(row[5]),2) #calculates the percentage
        reviews_percent.append(percent)             #returns the value o percent into the list
        new_length=row[9].split(" ")           #length is '4 hours' we are splitting the characters separated by " " and creating a new list ["4","hours"]
        length.append(float(new_length[0]))    #returning the first element splitted from the created list "4"
        
cleanCsv = zip(title,price,subscribers,reviews,reviews_percent,length) #Join all the lists together
outputFile = os.path.join(".","Resources","webFinal.csv")               #direction to the folder we want to store the new file

with open(outputFile,"w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title","Course Price", "Subscribrers","Reviews","Percent of reviews", "Length of Course"])
    writer.writerows(cleanCsv)

        




 


#    test = next(csvreader)

#print(length)

