from bs4 import BeautifulSoup
import requests
from utils import logger


def espn(url:str) -> any:
    """scrapes data from espn site

    Args:
        url (str): url to the site

    Returns:
        dict: dict{headline, body}
    """
    # user-agent required to avoid server error (mod_security)
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(response.text, 'lxml')

        # scrape by tags
        headings = soup.findAll('header', class_='article-header')
        paras = soup.findAll('p')
        headline_text = ' '.join([h.text for h in headings])
        body_text = ' '.join([p.text for p in paras])

        # store_results.store_result(headline_text=headline_text, body_text=body_text, url=url)
        # return {'Headline': headline_text, 'Content': body_text, 'Link': url}
        return headline_text, body_text, url
        
    except Exception as e:
        logger.log_message(f'Error: {e}', level=1)

def thedrive(url:str) -> any:
    """scrapes data from thedrive site

    Args:
        url (str): url to the site

    Returns:
        dict: dict{headline, body}
    """
    try:
        response = requests.get(url)
        soup2 = BeautifulSoup(response.text, 'lxml')

        # scrape by tags
        headings = soup2.findAll('section', class_='MuiBox-root css-0')[0:2]
        paras = soup2.findAll('p')

        headline_text = '\n'.join([h.text for h in headings])
        body_text = ' '.join([p.text for p in paras])

        # store_results.store_result(headline_text=headline_text, body_text=body_text, url=url)
        # {'Headline': headline_text, 'Content': body_text, 'Link': url}
        # return {'Headline': headline_text,'Content': body_text,'Link': url}
        return headline_text, body_text, url

    except Exception as e:
        logger.log_message(f'Error: {e}', level=1)