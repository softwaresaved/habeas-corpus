#!/usr/bin/env python
# coding: utf-8

# # CORD19 - enriching sample with DOIs/PIDs
# 
# The current two samples for the top 100, and 1000 items without the top 100, do not contain DOIs in their original form.
# 
# This notebook adds one DOI per item and writes the samples to a new version file.
# 
# What it does in detail is:
# 
# 1. Collect all PIDs for all instances of the exact software name from the original CORD-19 SM dataset
# 2. Add them to columns 'urls'
# 3. Pick one random PID
# 4. Add it to columns 'rand_url'
# 5. Trim the name strings in the process
# 6. Write the files
# 7. Remove columns 'urls' again
# 8. Save dataframes again to working copy files

import csv
import pandas as pd
import numpy as np
import random
import sys


# Define a function to convert "list strings" into lists
def str_to_list(list_string, separator):
    if isinstance(list_string, list):
        return list_string
    else:
        lst = list_string.replace('[', '').replace(']', '').replace("'", '').split(separator)
        return [s.strip() for s in lst]


# Set paths
top100_path = 'top_100.csv'
random1k_path = '1000sample_without_top_100.csv'
csm_path = '../cord-19/CORD19_software_mentions.csv'

# Prepare dataframes
df_csm = pd.read_csv(csm_path, converters={'software': pd.eval})

df_top100 = pd.read_csv(top100_path)
df_top100['urls'] = np.empty((len(df_top100), 0)).tolist()
df_top100['rand_url'] = pd.Series(dtype=str)

df_rand1k = pd.read_csv(random1k_path)
df_rand1k['urls'] = np.empty((len(df_rand1k), 0)).tolist()
df_rand1k['rand_url'] = pd.Series(dtype=str)

# Amend URLs in datasets, iterate the CSM once only!
for j, csm_row in df_csm.iterrows():
    if j % 10000 == 0:
        print('On iteration ', j)
    names = csm_row['software']
    urls = str_to_list(csm_row['url'], ';')
    # Iterate the other two dfs to match for names,
    # and append the list of URLs to the 'urls' list
    for i, top100_row in df_top100.iterrows():
        top100_name = top100_row['software']
        if top100_name in names:
            df_top100.at[i,'urls'].append(urls)
    for i, rand1k_row in df_rand1k.iterrows():
        rand1k_name = rand1k_row['software']
        if rand1k_name in names:
            df_rand1k.at[i,'urls'].append(urls)

# Save new files for backup
top100_urls_path = top100_path[:-4] + '_urls.bkup.csv'
df_top100.to_csv(top100_urls_path, encoding='utf8')
rand1k_urls_path = random1k_path[:-4] + '_urls.bkup.csv'
df_rand1k.to_csv(rand1k_urls_path, encoding='utf8')

# Pick a random entry in 'urls' and add to column
for i, top100_row in df_top100.iterrows():
    df_top100.at[i, 'rand_url'] = ';'.join(random.choice(str_to_list(top100_row['urls'], ',')))
for i, rand1k_row in df_rand1k.iterrows():
    df_rand1k.at[i, 'rand_url'] = ';'.join(random.choice(str_to_list(top100_row['urls'], ',')))

# Resave new files
top100_urls_path = top100_path[:-4] + '_urls.csv'
df_top100.to_csv(top100_urls_path, encoding='utf8')
rand1k_urls_path = random1k_path[:-4] + '_urls.csv'
df_rand1k.to_csv(rand1k_urls_path, encoding='utf8')

# Drop large 'urls' cells to create working copy files
df_top100.drop('urls', axis=1, inplace=True)
df_rand1k.drop('urls', axis=1, inplace=True)

# Save working copy files
df_top100.to_csv(top100_urls_path[:-4] + '_working_copy.csv', encoding='utf8')
df_rand1k.to_csv(rand1k_urls_path[:-4] + '_working_copy.csv', encoding='utf8')

sys.exit(0)