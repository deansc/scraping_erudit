import dateparser
import re
import urllib.request as urllib2
import vcr

from bs4 import BeautifulSoup

from lib.config import PathConfig
from lib.models import Article, Issue, Revue


class Scraper:
    def __init__(self, url, cassette_name):
        self.url = url
        self.cassette_name = cassette_name

        self.soup = self.get_soup()

    def get_soup(self):
        with vcr.use_cassette(f"fixtures/vcr_cassettes/{self.cassette_name}.yaml", record_mode="once"):
            response = urllib2.urlopen(self.url).read()
            return BeautifulSoup(response, "html.parser")

    @staticmethod
    def extract_issue(string):
        """
        input: Volume 7, numéro 2, 2020
        ouput: [7, 2, 2020]
        """
        to_return = {}
        for i in string.split(", "):
            if re.match(r".olume", i):
                to_return["volume"] = list(re.findall(r"\d+", i))[0]
            if re.match(r".uméro", i):
                to_return["number"] = list(re.findall(r"\d+", i))[0]
            if re.match(r".*(19|20)\d\d", i):
                to_return["year"] = list(re.findall(r"\d+", i))[0]
            if re.match(r"p\..+\d+.{1}\d+.*", i):
                to_return["pages"] = list(re.findall(r"\d+.{1}\d+", i))[0]
        return to_return


class ArticleScraper(Scraper):
    DOI_PATH = "https://doi.org/"
    model = Article()

    def scrap_and_assign(self):
        self.model.authors = self.get_authors()
        self.model.title = self.get_title()
        self.model.doi = self.get_doi()
        self.model.date = self.get_date()
        self.model.authors = self.get_authors()
        # print(self.get_title())
        # print(self.get_doi())
        # print(self.get_date())
        # print(self.get_issue_data())

    def get_authors(self):
        return [" ".join(li.span.text.split()) for li in self.soup.find_all("li", {"class": "doc-head__author"})]

    def get_title(self):
        return [li.span.text for li in self.soup.find_all("h1", {"class": "doc-head__title"})][0]

    def get_doi(self):
        aa = [li for li in self.soup.find_all("span", {"class": "hint--top hint--no-animate"})][-1]
        return aa.a["href"].replace(self.DOI_PATH, "")

    def get_date(self):
        aa = [i for i in self.soup.find_all("div", {"class": "doc-head__metadata"})][0]
        return dateparser.parse(aa.p.text.split(": ")[-1])

    def get_issue_data(self):
        # aa = [i for i in self.soup.find_all("div", {"class": "doc-head__metadata"})][1]
        aa = [i for i in self.soup.find_all("p", {"class": "refpapier"})][0]
        # return list(aa.children)[:-1]
        return aa.text


class IssueScraper(Scraper):
    model = Issue()

    def scrap_and_assign(self):
        for article_scraper in self.get_articles_scrapers():
            article_scraper.scrap_and_assign()
            break

    def get_articles_scrapers(self):
        for li in self._extract_articles_html():
            url = PathConfig.ERUDIT_PATH + li.h6.a["href"]
            issue = self.get_issue_number()
            article = [i for i in url.split("/") if i != ""][-1]

            iss = self.extract_issue(issue)
            cassette_name = "rmo/issue-" + f"{iss['volume']}-{iss['number']}-{iss['year']}" + "/" + article

            scraper = ArticleScraper(url=url, cassette_name=cassette_name)
            self.model.articles.append(scraper.model)
            scraper.model.issue = self.model

            yield scraper

    def get_issue_number(self):
        return self.soup.find_all("span", {"class": "issue-number"})[0].text

    def _extract_articles_html(self):
        for li in self.soup.find_all("li", {"class": "bib-record"}):
            yield li


class RevueScraper(Scraper):
    model = Revue()

    def scrap_and_assign(self):
        for issue_scraper in self.get_issue_scrapers():
            issue_scraper.scrap_and_assign()
            break

    def get_issue_scrapers(self):
        for li in self._extract_issues_html():
            url = PathConfig.ERUDIT_PATH + li.a["href"]
            issue = li.span.text

            iss = self.extract_issue(issue)
            cassette_name = "rmo/issue-" + f"{iss['volume']}-{iss['number']}-{iss['year']}"

            scraper = IssueScraper(url=url, cassette_name=cassette_name)
            self.model.issues.append(scraper.model)

            scraper.model.revue = self.model
            scraper.model.volume = iss["volume"]
            scraper.model.number = iss["number"]
            scraper.model.year = iss["year"]

            yield scraper

    def _extract_issues_html(self):
        for li in self.soup.find_all("li", {"class": "issue-list__item"}):
            yield li
