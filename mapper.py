import argparse
import csv
import pandas as pd
import vcr

from lib.sparql import Sparql
from lib.wikidata import WikidataP as P, WikidataRow as Row

revue_qids = {"rmo": "Q13442814"}

query = """
SELECT ?article ?articleLabel ?doi WHERE {
  ?article wdt:P31 wd:Q13442814;
    wdt:P1433 wd:Q47523513 .
  ?article wdt:P356 ?doi.

  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "fr,en".
  }
}
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map local scraped articles with their Wikidata equivalents.")
    parser.add_argument("-r", "--revue", required=True)
    parser.add_argument("-q", "--query", required=True)
    args = parser.parse_args()

    print(args)

    df = pd.read_csv("fixtures/csv_outputs/rmo_articles.csv")
    print(len(df.index))

    # list_of_list = []
    # list_of_list.append(["qid", f"-{P.DOI}", P.DOI])

    # with vcr.use_cassette(f"fixtures/vcr_cassettes/{args.revue}_sparql/{args.query}.yaml", record_mode="once"):
    #     sparl = Sparql()
    #     results = sparl.execute(query)

    #     for result in results["results"]["bindings"]:
    #         qid = result["article"]["value"].split("/")[-1]
    #         label = result["articleLabel"]["value"]
    #         doi = result["doi"]["value"]

    #         doi_uppercased = doi.upper()

    #         print(f"{qid} {doi} {doi_uppercased}")
    #         # list_of_list.append([qid, Row.stringify(doi), Row.stringify(doi_uppercased)])

    # with open(f"fixtures/csv_outputs/{args.revue}_articles_doi_uppercased.csv", "w", newline="") as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerows(list_of_list)
