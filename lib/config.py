class PathConfig:
    ERUDIT_PATH = "https://www.erudit.org"
    REVUE_URL = ERUDIT_PATH + "/fr/revues"

    @staticmethod
    def back_issues_url(revue):
        return f"{PathConfig.REVUE_URL}/{revue}/#back-issues"
