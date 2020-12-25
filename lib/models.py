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
