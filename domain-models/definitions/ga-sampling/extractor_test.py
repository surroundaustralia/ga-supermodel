from rdflib import Graph, Namespace

test_data = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX ex: <http://example.com/>
PREFIX gas: <http://pid.geoscience.gov.au/def/ga-samples/>
PREFIX geo: <http://www.opengis.net/ont/geosparql>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX tern: <https://w3id.org/tern/ontologies/tern/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

ex:sample-1
    a tern:MaterialSample ;
    ex:label "Example Label" ;
    gas:dateAcquired "2000-01-01"^^xsd:date ;
    gas:samplingLocation [
            a geo:Geometry ;
            geo:asWKT "POINT (1 1)"^^geo:wktLiteral
        ] ;
    dcterms:created "2000-01-02"^^xsd:date ;
.

ex:thing-x
    a owl:Thing ;
    rdfs:comment "Some other, ireelevant, class instance" ;
.
"""
g = Graph().parse(data=test_data)

q = """
PREFIX gas: <http://pid.geoscience.gov.au/def/ga-samples/>
PREFIX tern: <https://w3id.org/tern/ontologies/tern/>


CONSTRUCT {
    ?ms a tern:MaterialSample ;
        gas:samplingLocation [
            geo:asWKT ?wkt ;
        ] ;
        gas:dateAcquired ?date_aquired ;
}
WHERE {
    ?ms a tern:MaterialSample ;
        gas:samplingLocation ?sampling_location ;
        gas:dateAcquired ?date_aquired ;
    .

    ?sampling_location geo:asWKT ?wkt .
}
"""
print("results:")
g2 = g.query(q)
print(type(g2))
g3 = Graph().parse(g2.serialize())
g3.bind("gas", "http://pid.geoscience.gov.au/def/ga-samples/")
g3.bind("geo", "http://www.opengis.net/ont/geosparql")
# print(g3.serialize())
print(type(g3))