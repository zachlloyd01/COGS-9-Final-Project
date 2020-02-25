#Written by Zachary Lloyd, 2/25/2020
#For UCSD COGS 9 class with Bradley Voytek
#Data minification for final project

import csv #Default library, as Pandas is not required for something this simple

with open('data/FullSet.csv', 'r', encoding='utf-8') as f: #Open the Full Dataset

    csv_reader = csv.DictReader(f, delimiter=',') #Create a reader object, will output an orderedDict() object

    outFile = open('data/MinSet.csv', 'w', encoding='utf-8', newline='') #Define the output file

    fieldnames = ['duration_ms', 'danceability', 'speechiness', 'popularity'] #The fields to be written to the output file

    writer = csv.DictWriter(outFile, fieldnames=fieldnames) #Define a new CSV-Writer to write the orderedDict() created from csv_reader to the output file

    writer.writeheader() #Write the headers to the output file (defined in fieldnames)

    for row in csv_reader: #For every row in the FullSet file

        if row['\ufeffgenre'] == "R&B": #If the genre is R&B (Yes, weird name for the column header. Ask Kaggle, was their crappy program)

            writer.writerow({'duration_ms': f"{row['duration_ms']}", 'danceability': f"{row['danceability']}", 'speechiness': f"{row['speechiness']}", 'popularity': f"{row['popularity']}"}) #Write the parts of the dictionary we actually care about into the file