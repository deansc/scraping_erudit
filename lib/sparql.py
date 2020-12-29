from SPARQLWrapper import JSON, SPARQLWrapper


class Sparql:
    ENDPOINT1 = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    ENDPOINT2 = "https://query.wikidata.org/sparql"

    def __init__(self):
        self.sparql = SPARQLWrapper(self.ENDPOINT2)
        self.sparql.setReturnFormat(JSON)

    def execute(self, query):
        self.sparql.setQuery(query)
        return self.sparql.query().convert()
