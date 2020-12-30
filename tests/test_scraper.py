import unittest

from lib.scrapers import Scraper


class TestScraper(unittest.TestCase):
    def test_extract_issue(self):
        string = "Volume 7, numéro 20, 2020"
        response = Scraper.extract_issue(string)

        self.assertEqual(len(response.keys()), 3)

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

    def test_extract_issue_when_pages_messed_up(self):
        string = "Volume 7, Numéro 2, 2020, p. 1–20Fenêtre ouverte sur la médiation de la musique"
        response = Scraper.extract_issue(string)

        self.assertEqual(len(response.keys()), 4)

        self.assertEqual(response["volume"], "7")
        self.assertEqual(response["number"], "2")
        self.assertEqual(response["year"], "2020")
        self.assertEqual(response["pages"], "1–20")

    def test_generate_cassette_prefix(self):
        prefix = Scraper.generate_cassette_prefix(year="2323", volume="1", number="44")
        self.assertEqual(prefix, "issue-44-1-2323")

        prefix = Scraper.generate_cassette_prefix(year="2323", volume="1", number=None)
        self.assertEqual(prefix, "issue-1-2323")

        prefix = Scraper.generate_cassette_prefix(year="2323", volume=None, number="44")
        self.assertEqual(prefix, "issue-44-2323")

        prefix = Scraper.generate_cassette_prefix(year="2323", volume=None, number=None)
        self.assertEqual(prefix, "issue-2323")
