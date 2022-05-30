def main():
    #importing required libraries. 
    import os
    import csv
    import json
    #creating an iteratable directory list.
    
    directory_list= os.listdir(r'D:\Coding Projects\Hockey Stats\DraftYear.csv\\')
    csvFileFolder = r'D:\Coding Projects\Hockey Stats\DraftYear.csv'
    jsonFileFolder = r'D:\Coding Projects\Hockey Stats\DraftYear.json'
    i = 1983

    def csv_to_json(csvFilePath, jsonFilePath):
        jsonArray = []
        #opens .csv file and adds each row to the json array.
        with open(csvFilePath) as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                jsonArray.append(row)

        #converts json array into .json file
        with open(jsonFilePath, 'w') as jsonf:
            jsonString =json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)
    
    for files in directory_list:
        while i < 2021:
            i=i+1
            csvFilePath = csvFileFolder + "\Hockey"+ str(f'{i}')+".csv"
            jsonFilePath = jsonFileFolder+"\Hockey"+ str(f'{i}')+ ".json"
            csv_to_json(csvFilePath,jsonFilePath)

if __name__ == '__main__':
    main()