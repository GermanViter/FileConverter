import os   
import sys
import json 

filePath = input("Enter the file path: ")
jsonFilePath = input("Enter the jason file path : ")

if not os.path.exists(filePath): 
    print("Error: file not found")
    sys.exit()

lines = []
lineCount = 0
words = []




with open(filePath, "r") as f:
    for line in f:
        values = line.strip().split(',')
        if lineCount == 0:
            for i in values:
                words.append(i)
        else:
            wordCount = 0
            dict1 = {}
            for word in values:
                try:
                    dict1.update({words[wordCount]:word})
                    wordCount += 1
                except IndexError:
                    print("The number of keys does not match number of values")
                    sys.exit()
            lines.append(dict1)
        lineCount += 1

with open(jsonFilePath, "w") as js:
    json.dump(lines, js, indent=4)


print("Data has been successfully converted to JSON format and saved to the specified file.")
