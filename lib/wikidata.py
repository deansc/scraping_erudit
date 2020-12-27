from lib.models import Article


class WikidataP:
    IS_A = "P31"
    TITLE = "P1476"
    LANGUAGE = "P407"
    PUBLICATION_DATE = "P577"
    PUBLISHED_IN = "P1433"
    VOLUME = "P478"
    PAGES = "P304"
    NUMBER = "P433"
    DOI = "P356"

    AUTHORS_STR = "P2093"
    AUTHORS_OBJ = "P50"
    RANK_QAL = "qal1545"
    STATED_AS = "P1932"


class WikidataQ:
    IS_A = "Q13442814"
    PUBLISHED_IN = "Q47523513"
    LANGUAGE = "Q150"


class WikidataRow:
    """
    "qid","Lfr","Dfr","P31","P1476","P179","qal1545","P4908","qal1545","P136","P449","P495","P364","P577","P973","qal407","P856","qal407","P1651"
    """

    HEADER = [
        "qid",
        "Lfr",
        "Dfr",
        "Len",
        "Lnl",
        WikidataP.IS_A,
        WikidataP.LANGUAGE,
        WikidataP.TITLE,
        WikidataP.PUBLICATION_DATE,
        WikidataP.PUBLISHED_IN,
        WikidataP.VOLUME,
        WikidataP.PAGES,
        WikidataP.NUMBER,
        WikidataP.DOI,
        WikidataP.AUTHORS_STR,  # at the end so we can have multiple?
        WikidataP.RANK_QAL,
    ]

    def __init__(self, article):
        self.article = article
        self.row = []

    @staticmethod
    def stringify(string):
        return f'"{string}"'

    def get_row(self):
        if self.article.title == "Présentation du numéro":
            title = self.article.title + " « " + self.article.issue.title + " »"
        else:
            title = self.article.title

        try:
            author_1 = self.stringify(self.article.authors[0])
            rank_1 = self.stringify("1")
        except IndexError:
            author_1 = None
            rank_1 = None

        row = [
            "",  # qid
            title,  # "Lfr",
            "article paru dans Revue musicale OICRM",  # "Dfr",
            title,  # "Len",
            title,  # "Lnl",
            WikidataQ.IS_A,  # WikidataP.IS_A,
            WikidataQ.LANGUAGE,  # WikidataP.LANGUAGE,
            f"fr:{self.stringify(title)}",  # WikidataP.TITLE,
            self.article.date.strftime("+%Y-%m-%dT00:00:00Z/11"),  # WikidataP.PUBLICATION_DATE,
            WikidataQ.PUBLISHED_IN,  # WikidataP.PUBLISHED_IN,
            self.stringify(self.article.issue.volume),  # WikidataP.VOLUME,
            self.stringify(self.article.pages),  # WikidataP.PAGES,
            self.stringify(self.article.issue.number),  # WikidataP.NUMBER,
            self.stringify(self.article.doi),  # WikidataP.DOI,
            author_1,  # WikidataP.AUTHORS_STR,  # at the end so we can have multiple?
            rank_1,  # WikidataP.RANK_QAL,
        ]

        return row
