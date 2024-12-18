def build_search_query(search_term):
    return f"""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        
        SELECT DISTINCT ?entity ?label ?description
        WHERE {{
            ?entity rdfs:label ?label ;
                   dbo:abstract ?description .
            FILTER (LANG(?label) = "en")
            FILTER (LANG(?description) = "en")
            FILTER (REGEX(?label, "{search_term}", "i"))
        }}
    """