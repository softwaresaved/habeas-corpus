import csv
import pandas
import random

SAMPLE_COUNT = 100

i = 0
with open('../cord-19/CORD19_software_mentions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        i += 1
    
n = i #number of records in file
s = 100 #desired sample size
filename = "../cord-19/CORD19_software_mentions.csv"
skip = sorted(random.sample(range(n),n-s))
df = pandas.read_csv(filename, skiprows=skip)
df.to_csv('output.csv', sep=',')
