get_license_from_repo_addr <- function(repo)
{
    blank_return <- c(license_key = NA, 
                      license_name = NA, 
                      license_url = NA)

    if (is.na(repo))
    {
        return(blank_return)
    }
        
    resp <- tryCatch(
        gh("GET /repos/{repo}/license", repo = repo), 
        error = function(e) {
            message("could not retrieve info for ", repo)
            return(NULL)
        }
    )
    if (is.null(resp)) # failed to retrieve info from github
    {
        return(blank_return)
    }
    
    c(license_key = resp$license$key, 
      license_name = resp$license$name, 
      license_url = resp$license$url)
}
