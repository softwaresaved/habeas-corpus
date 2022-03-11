#!/usr/bin/env python
# coding: utf-8

# # CORD19 - enriching sample with DOIs/PIDs
# 
# The current two samples for the top 100, and 1000 items without the top 100,
# do not contain DOIs in their original form.
# 
# This notebook adds one DOI per item and writes the samples to a new version file.
# 
# What it does in detail is:
# 
# 1. Collect all names from each df and store in dicts as keys
# 2. Iterate the CSM, check for matching names in 'software' columns, add list of URLs to respective dict
# 3. Iterate over each sample df, add urls to 'urls' column, and pick one url list to add to 'rand_url column'
# 4. Save, then drop the urls column for a working copy, save that as well

import csv
import pandas as pd
import numpy as np
import random
import sys
import logging
from datetime import datetime
import time

# Configure logging
logfile = datetime.now().strftime('%Y-%m-%d_%H-%M_') + 'add-urls.log'
logging.basicConfig(filename=logfile,
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Define a function to convert "list strings" into lists
def str_to_list(list_string, separator):
    if isinstance(list_string, list):
        return list_string
    else:
        lst = list_string.replace('[', '').replace(']', '').replace("'", '').split(separator)
        return [s.strip() for s in lst]


# Set paths
top100_path = 'top_100.csv'
rand1k_path = '1000sample_without_top_100.csv'
csm_path = '../cord-19/CORD19_software_mentions.csv'

start = time.time()

df_top100 = pd.read_csv(top100_path)

df_rand1k = pd.read_csv(rand1k_path)

top100_names = dict(zip(df_top100['software'], ([] for _ in df_top100['software'])))
rand1k_names = dict(zip(df_rand1k['software'], ([] for _ in df_rand1k['software'])))

df_csm = pd.read_csv(csm_path, converters={'software': pd.eval})


for i, csm_row in df_csm.iterrows():
    if i % 10000 == 0:
        print('On iteration ', i)
    names = csm_row['software']
    urls = str_to_list(csm_row['url'], ';')
    logging.info(f'Row {i}: - names: {names} - URLs: {urls}')
    for name in names:
        if name in top100_names.keys():
            logging.info(f'Found name {name} from CSM row {i} in top 100')
            top100_names[name].append(urls)
        if name in rand1k_names.keys():
            logging.info(f'Found name {name} from CSM row {i} in rand 1000')
            rand1k_names[name].append(urls)


def rand_url(row):
    return ';'.join(random.choice(str_to_list(row['urls'], ',')))


def apply_urls(df, dct):
    df['urls'] = df['software'].map(dct)
    df['rand_urls'] = df.apply(lambda row: rand_url(row), axis=1)


apply_urls(df_top100, top100_names)
apply_urls(df_rand1k, rand1k_names)

# Save working copy files
df_top100.to_csv(top100_path[:-4] + '_urls.csv', encoding='utf8')
df_rand1k.to_csv(rand1k_path[:-4] + '_urls.csv', encoding='utf8')

# Drop large 'urls' cells to create working copy files
df_top100.drop('urls', axis=1, inplace=True)
df_rand1k.drop('urls', axis=1, inplace=True)

# Save working copy files
df_top100.to_csv(top100_path[:-4] + '_urls_working_copy.csv', encoding='utf8')
df_rand1k.to_csv(rand1k_path[:-4] + '_urls_working_copy.csv', encoding='utf8')
print(f'Ran for {time.time() - start} seconds')

sys.exit(0)