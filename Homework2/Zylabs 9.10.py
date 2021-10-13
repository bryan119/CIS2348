#Bryan Nguyen
#1855265

import csv
file_csv = input()
with open(file_csv, 'r') as file:
    csv_reader = csv.reader(file)
    words = dict()
    for i in csv_reader:
        for j in i:
            if j in words:
                words[j] = words[j] + 1
            else:
                words[j] = 1

    for k in list(words.keys()):
        print(k, words[k])