library(gh)
library(stringr)

source(here::here("R/github-lookup-functions.R"))

input_file <- here::here("data/output/CORD19_software_popularity_sampled_QA_DOI.csv")

bare_filename <- basename(input_file)
output_filename <- sub("(\\.\\w+)$", "_license\\1", bare_filename)
output_file <- here::here(dirname(input_file), output_filename)

# check for github PAT and error if it is not set ----
# this prevents rate-limiting from otherwise halting execution

if (gh_token() == "")
{
    stop("No GitHub PAT detected; please set one before running this script; see https://usethis.r-lib.org/articles/articles/git-credentials.html for more info.")
}

# read in cleaned data ----
data_in <- read.csv(input_file)

# look up license info using github API ----
repo_column <- "CodeRepository"
pattern <- "github.com/(\\w+/\\w+)"
repo_addr <- str_match(data_in[[repo_column]], pattern)[,2]
license_data <- do.call(rbind, lapply(repo_addr, get_license_from_repo_addr))

# merge license info and write out
data_out <- cbind(data_in, license_data)
write.csv(data_out, output_file, row.names = FALSE, quote = FALSE)
