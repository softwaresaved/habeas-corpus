import csv
import pandas
import random

SAMPLE_COUNT = 100

i = 0
with open('../cord-19/CORD19_software_mentions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    row_count = sum(1 for row in csv_reader)
    rand_ints = random.sample(range(1, row_count), SAMPLE_COUNT)
    with open('output.csv', 'w') as output:
        output_writer = csv.writer(output, delimiter=',')
        csv_file.seek(0)
        for row in csv_reader:
            if i == 0 or i in rand_ints:
                output_writer.writerow(row)
            i += 1


