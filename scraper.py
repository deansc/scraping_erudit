from lib.config import PathConfig
from lib.scrapers import RevueScraper


if __name__ == "__main__":
    revue_scraper = RevueScraper(url=PathConfig.RMO_ISSUES_URL, cassette_name="rmo/back-issues")
    revue_scraper.scrap_and_assign()
    revue = revue_scraper.model

    for issue in revue.issues:
        for article in issue.articles:
            print(article)
