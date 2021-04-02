library(gh)
library(stringr)

source(here::here("R/github-lookup-functions.R"))

# check for github PAT and error if it is not set ----
# this prevents rate-limiting from otherwise halting execution

if (gh_token() == "")
{
    stop("No GitHub PAT detected; please set one before running this script; see https://usethis.r-lib.org/articles/articles/git-credentials.html for more info.")
}

# read in cleaned data ----
data_file <- here::here("data/output/CORD19_sampled_with_repos.csv")
data_in <- read.csv(data_file)

# look up license info using github API ----
pattern <- "github.com/(\\w+/\\w+)"
repo_addr <- str_match(data_in$Code.Repository, pattern)[,2]
license_data <- do.call(rbind, lapply(repo_addr, get_license_from_repo_addr))

# merge license info and write out
data_out <- cbind(data_in, license_data)
output_file <- here::here("data/output/CORD19_sampled_with_repos_with_github-metadata.csv")
write.csv(data_out, output_file, row.names = FALSE, quote = FALSE)
