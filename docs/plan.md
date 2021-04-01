# Plan

## Basic plan

0. Come up with a great bacronym for _Habeas_ e.g. Helpfully Annotated Basic Encyclopedia of Academic Software  
1. Take the CORD-19 Software Mentions dataset and clean it
2. Sort the dataset in order of popularity
3. Starting with the most popular software, split the software between us and manually identify whether the software has an associated code repository
4. Create the first _Habeas Corpus_ from this exercise, which will just contain: name of the software, URL of associated code repository, list of identifiers of papers that mention it
5. Use this version of _Habeas Corpus_ to test analyses that answer the questions we'd like to pose, and identify what information/metadata is missing
6. Go back to incorporate that metadata where simple
7. Present some of the questions we're now able to answer using _Habeas Corpus_

## Stretch goals

- Based on our experience of 1. create instructions for cleaning the CORD-19 Software Mentions dataset
- Based on our experience of 1. create a "software name deduplication mapping tool" which lets people know the aliases of common software titles
- Create entries in Wikidata for each piece software, including its aliases, to give it a unique identifier
- Create tools to make it easier to automatically 

## Suggested analyses

|Question|Data / Metadata required|Notes|
|--------|------------------------|-----|
|Most popular software|Software mentions, software aliases|
|Usage| ? |How do we identify number of users? Number of unique publication authors who mention it? Number of unique publications that mention it?|
|Type of License| Link to code repository or license file | Should this be dynamically fetched? |
|Filter software by purpose|?| Requires classification of purpose |
|How software is being used| Where software is mentioned, other context? | Is there a good way of doing this in an automated way? |
|Analyse dependencies| Link to code repo | |
|Software metrics| Link to code repo | |
|Software project metrics (e.g. how often developed, contributors) | Link to code repo | |
|Academic disciplines a piece of software is used in | Links to paper IDs that mention it | |
|Who funded the software | Links to grants, funders | Perhaps through acknowledgements in the paper that mentions it? Only works if author created |
|Who funded the use of the software to do a piece of research| Link to paper ID and ability to extract research funder info from that |
|How detailed is the mention of the software (e.g. citation, version number, release year)| Full text encoding? | This might be better applied to the SoftCite dataset which has this information already coded and annotated|
|Summarise by platform, e.g. all Python packages | Platform metadata | Or some external source that allows understanding of what software is "similar" |

## Suggested Annotation Format

* Software Title (String)
* Number of unique papers that mention it at least once (Integer)
* Link to code repository (if available) (URI)
* List of papers which mention software title (list of DOIs/URIs)
* List of titles that map to this (list of Strings)

### Information we want to derive from this data

- Dependencies: we could create a utility that leverages [GitHub's support for understanding dependencies](https://docs.github.com/en/code-security/supply-chain-security/exploring-the-dependencies-of-a-repository)
- License type: we could use existing utilities for finding the license of a GitHub repo
- Academic disciplines: we could create a tool that extracts JATS4R Subject and Keyword tags: https://www.niso.org/publications/rp-32-2019-jats4r-subjects-and-keywords-v1
- Funders: we could use PID Graph / OpenAIRE funder database, or scrape from papers

### Other databases that we could combine that allow us to answer more questions

- What software is used on national Tier-1 / Tier-2 facilities
- What software depends / is a dependency of this
- Canonical list of disciplines
- Wikidata


