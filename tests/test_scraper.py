import unittest

from lib.scrapers import Scraper


class TestScraper(unittest.TestCase):
    def test_extract_issue(self):
        string = "Volume 7, numéro 20, 2020"
        response = Scraper.extract_issue(string)

        #self.assertEqual(len(response.keys()), 3)

        self.assertEqual(response["volume"], "7")
        self.assertEqual(response["number"], "20")
        self.assertEqual(response["year"], "2020")

    def test_extract_issue_when_season(self):
        string = "Volume 1, numéro 1, automne 1992"
        response = Scraper.extract_issue(string)

        self.assertEqual(len(response.keys()), 3)

        self.assertEqual(response["volume"], "1")
        self.assertEqual(response["number"], "1")
        self.assertEqual(response["year"], "1992")

    def test_extract_issue_when_pages_no_volume(self):
        string = "Numéro 33, 2008, p. 5-183"
        response = Scraper.extract_issue(string)

        self.assertEqual(len(response.keys()), 3)

        self.assertEqual(response["number"], "33")
        self.assertEqual(response["year"], "2008")
        self.assertEqual(response["pages"], "5-183")
