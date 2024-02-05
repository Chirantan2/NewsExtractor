from utils import chooseSource, logger
import json 
import os
import pandas as pd
import timeit

PATH = os.path.dirname(os.path.abspath('__file__'))

def main():
    logger.log_message('Start', level=0)
    
    try:
        # load urls from config.json
        with open(PATH+r'\config.json') as fp:
            urls = json.load(fp)
            # urls = configs['media_url']
        # results = []

        # scrape each url
        for url in urls:
            logger.log_message(f"Scraping - {url}", level=0)
            data = chooseSource.source_select(url)
            # results.append(data)
        
        # output csv file
        # df = pd.DataFrame(results)
        # df.to_csv('news.txt')
    except Exception as e:
        logger.log_message(f"Error - {e}", level=1)

if __name__ == '__main__':
    starting_time = timeit.default_timer()
    main()
    logger.log_message(f"End", level=0)
    logger.log_message(f'Execution Time: {timeit.default_timer() - starting_time}', level=0)
    
