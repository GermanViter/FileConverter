import os   
import sys
import json 
import csv

def csvToJson():
    filePath = input("Enter the file path: ")
    if not os.path.exists(filePath): 
        print("Error: file not found")
        sys.exit()

    isValidCSV(filePath)

    jsonFilePath = input("Enter the jason file path : ")
    isValidJSON(jsonFilePath)   

    separator = input("Enter the separator used in the CSV file (default is ','): ")
    if separator == "":
        separator = ","

    dicts = []
    lineCount = 0
    words = []
    nbrKeys = 0

    with open(filePath, "r") as f:
        lines = csv.reader(f, delimiter=separator)
        for line in lines:
            if lineCount == 0:
                for i in line:
                    words.append(i)
                    nbrKeys += 1
            else:
                if len(line) < nbrKeys:
                    print("Error : The number of lines is less than the number of keys")
                    sys.exit(1)
                wordCount = 0
                dict1 = {}
                for word in line:
                    try:
                        dict1.update({words[wordCount]:word})
                        wordCount += 1
                    except IndexError:
                        print("Error: The number of lines in line {} does not match the number of headers.".format(lineCount + 1))
                        sys.exit()
                dicts.append(dict1)
            lineCount += 1
        if lineCount == 1 or lineCount == 0:
            print("Error: The CSV file is empty or only contains headers.")
            sys.exit(1)
    with open(jsonFilePath, "w") as js:
        json.dump(dicts, js, indent=4)
    print("Data has been successfully converted to JSON format and saved to the specified file.")

def jsonToCsv():
    filePath = input("Enter the file path: ")
    if not os.path.exists(filePath): 
        print("Error: file not found")
        sys.exit()

    isValidJSON(filePath)

    csvFilePath = input("Enter the CSV file path : ")
    isValidCSV(csvFilePath)

    with open(filePath, "r") as f:
        data = json.load(f)
    separator = input("Enter the separator to use in the CSV file (default is ','): ")
    if separator == "":
        separator = ","
    with open(csvFilePath, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=separator)
        if len(data) > 0:
            headers = data[0].keys()
            writer.writerow(headers)
            for item in data:
                writer.writerow(item.values())
            print("Data has been successfully converted to CSV format and saved to the specified file.")
        else:
            print("Error: The JSON file is empty.")
            sys.exit(1)

def main():
    while True:
        print("Welcome to the CSV-JSON converter!")
        print("Please select an option:")
        print("1. Convert CSV to JSON")
        print("2. Convert JSON to CSV")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            csvToJson()
        elif choice == "2":
            jsonToCsv()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")
        

def isValidCSV(filePath):
    if not filePath.endswith('.csv'):
        print("Error: Invalid file format. Please provide a .csv file.")
        sys.exit(1)

def isValidJSON(filePath):
    if not filePath.endswith('.json'):
        print("Error: Invalid file format. Please provide a .json file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
