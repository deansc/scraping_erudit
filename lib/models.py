from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Revue:
    issues: list = field(default_factory=list)


@dataclass
class Issue:
    revue: Revue = None
    articles: list = field(default_factory=list)
    volume: str = None
    number: str = None
    year: str = None


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
