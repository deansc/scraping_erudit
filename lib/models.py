from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Revue:
    issues: list = field(default_factory=list)
    title: str = None

    def issues_count(self):
        return len(self.issues)

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "title": self.title,
            "issues": self.issues_count(),
        }


@dataclass
class Issue:
    revue: Revue = None
    articles: list = field(default_factory=list)
    title: str = None
    volume: str = None
    number: str = None
    year: str = None

    def articles_count(self):
        return len(self.articles)

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "title": self.title,
            "articles": self.articles_count(),
        }


@dataclass
class Article:
    issue: Issue = None
    authors: list = field(default_factory=list)
    date: datetime = None
    title: str = None
    pages: str = None
    url: str = None
    doi: str = None

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "pages": self.pages,
            "doi": self.doi,
            "url": self.url,
            "volume": self.issue.volume,
            "number": self.issue.number,
            "year": self.issue.year,
        }
