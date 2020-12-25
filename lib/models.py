from dataclasses import dataclass, field


@dataclass
class Revue:
    issues: list = field(default_factory=list)


@dataclass
class Issue:
    volume: str = None
    number: str = None
    year: str = None
    articles: list = field(default_factory=list)


@dataclass
class Article:
    authors: list = field(default_factory=list)
    date: str = None
    title: str = None
    pages: str = None
    url: str = None
    doi: str = None
