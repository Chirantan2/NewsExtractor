from utils.scraper import thedrive, espn
def source_select(url):
    """Separates the domain name from the url and calls the domain specific function or else raises an error if the function doesn't exist

    Args:
        url (_type_): url of the site

    Raises:
        ValueError: If no function exists for that particular domain 

    Returns: Calls the url specific function
    """
    
    # get function name from url
    domain = url.split('/')[2] if '://' in url else url.split('/')[0] 
    function_name = f"{domain.split('.')[1]}"

    try:
        # call function dynamically
        return eval(f"{function_name}('{url}')")
    except NameError as e:
        raise ValueError(f"Error: {e}")