from SPARQLWrapper import SPARQLWrapper, JSON
from utils.query_builder import build_search_query

class DBPediaService:
    def __init__(self):
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        self.sparql.setReturnFormat(JSON)

    def search_entity(self, search_term):
        query = build_search_query(search_term)
        self.sparql.setQuery(query)
        
        try:
            results = self.sparql.query().convert()
            return self._process_results(results)
        except Exception as e:
            raise Exception(f"Error querying DBPedia: {str(e)}")

    def _process_results(self, results):
        processed_results = []
        for result in results["results"]["bindings"]:
            processed_results.append({
                'uri': result.get('entity', {}).get('value', ''),
                'label': result.get('label', {}).get('value', ''),
                'description': result.get('description', {}).get('value', '')
            })
        return processed_results