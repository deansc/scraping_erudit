import csv

from lib.config import PathConfig
from lib.scrapers import RevueScraper
from lib.wikidata import WikidataRow

if __name__ == "__main__":
    revue = "rmo"
    url = PathConfig.back_issues_url(revue)

    revue_scraper = RevueScraper(revue=revue, url=url, cassette_name="back-issues")
    revue_scraper.scrap_and_assign()
    revue = revue_scraper.model

    list_of_list = []
    list_of_list.append(WikidataRow.HEADER)
    print(WikidataRow.HEADER)

    for issue in revue.issues:
        # print(issue)
        for article in issue.articles:
            if len(article.authors) == 1:  # TODO: in the future we process authors separately
                w = WikidataRow(article=article)
                row_to_write = w.get_row()
                list_of_list.append(row_to_write)
                print(row_to_write)

    with open("output.csv", "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(list_of_list)
