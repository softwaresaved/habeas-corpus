#!/bin/bash
# -----
# Retrieves and prepares the data for CSM
# -----

# Prepare data directory
mkdir ./v5/data

# Retrieve the CORD-19 Software Mentions dataset from datadryad
wget https://datadryad.org/stash/downloads/download_resource/108159
mkdir ./v5/data/csm
unzip 108159 -d ./v5/data/csm/
