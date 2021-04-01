# Output files

This directory contains processed files based on the original CORD-19 software mentions dataset. These datasets are released by the project under a CC0 license.

The files are:

   - CORD19_software_popularity.csv: The CORD-19 software mentions dataset, processed to count the number of unique papers which mention each "software" in the dataset 
   - CORD19_software_popularity_sampled_QA.csv: The result of manually checking and annotating a random sample of 100 software titles from CORD19_software_popularity.csv
   - CORD19_sampled_with_repos.csv: A subset of CORD19_software_popularity_sampled_QA.csv, containing those where the software had a code repository which could be identified.
