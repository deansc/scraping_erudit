from lib.config import PathConfig
from lib.scrapers import RevueScraper


if __name__ == "__main__":
    revue_scraper = RevueScraper(url=PathConfig.RMO_ISSUES_URL, cassette_name="rmo/back-issues")

    for issue_scraper in revue_scraper.get_issue_scrapers():
        for article_scraper in issue_scraper.get_articles_scrapers():
            # print(article_scraper.soup)
            # print(article_scraper.url)
            print(article_scraper.get_authors())
            print(article_scraper.get_title())
            print(article_scraper.get_doi())
            print(article_scraper.get_date())
            print(article_scraper.get_issue_data())
            break
        break
