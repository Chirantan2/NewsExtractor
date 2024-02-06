from utils.chooseSource import source_select
from utils.logger import log_message
from utils.store_results import store_result
import json 
import os
import timeit


PATH = os.path.dirname(os.path.abspath('__file__'))

def main():
    with open('output.txt', 'w', encoding='UTF-8') as file:
        file.write('')

    log_message('Start', level=0)
    try:
        # load urls from config.json
        with open('config.json') as fp:
            urls = json.load(fp)

        # scrape each url
        for url in urls:
            log_message(f"Scraping - {url}", level=0)
            headline, content, link = source_select(url)
            store_result(headline, content, link)  
            # store_results.store_result(list)

        # text = ""
        # for k, v in dict.items():
        #     text += "URL: " + k
        #     text += "\nTITLE: " + v['title'] + \
        #         "\nCONTENT: " + \
        #         v['body'] + "\n\n" + "="*200 + "\n\n"  
        # with open("output.txt", 'w') as f:
        #     f.write(text)
        
    except Exception as e:
        log_message(f"Error - {e}", level=1)

if __name__ == '__main__':
    starting_time = timeit.default_timer()
    main()
    log_message(f"End", level=0)
    log_message(f'Execution Time: {timeit.default_timer() - starting_time}', level=0)
    
