Scraping Erudit.org

This thing scraps all the articles (not the content, just the metadata) of a given publication in erudit.org. It was mostly developped to export data into Wikidata.


Running test:

```
python -m unittest tests/test_scraper.py
```


Blackify:
```
black -l120 -tpy37 .
```


Run the script:
```
python scraper.py
```