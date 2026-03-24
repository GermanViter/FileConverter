import os   
import sys
import json 



def csvToJson():
    filePath = input("Enter the file path: ")
    if not os.path.exists(filePath): 
        print("Error: file not found")
        sys.exit()

    isValidCSV(filePath)

    jsonFilePath = input("Enter the jason file path : ")
    isValidJSON(jsonFilePath)   

    lines = []
    lineCount = 0
    words = []
    nbrKeys = 0



    with open(filePath, "r") as f:
        for line in f:
            values = line.strip().split(',')
            if lineCount == 0:
                for i in values:
                    words.append(i)
                    nbrKeys += 1
            else:
                if len(values) < nbrKeys:
                    print("Error : The number of values is less than the number of keys")
                    sys.exit(1)
                wordCount = 0
                dict1 = {}
                for word in values:
                    try:
                        dict1.update({words[wordCount]:word})
                        wordCount += 1
                    except IndexError:
                        print("Error: The number of values in line {} does not match the number of headers.".format(lineCount + 1))
                        sys.exit()
                lines.append(dict1)
            lineCount += 1

    with open(jsonFilePath, "w") as js:
        json.dump(lines, js, indent=4)


    print("Data has been successfully converted to JSON format and saved to the specified file.")

def main():
    csvToJson()


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
