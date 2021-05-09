import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?child ?weight ?age WHERE {
        ?subject a ?person .
        FILTER( STRSTARTS(STR(?person),str(g:Father)) ) .
        ?subject g:hasChild ?child .
        ?child g:weight ?weight .
        ?child g:hasAge ?age .
    }
    ORDER BY ASC(?age)
    """)
for row in qres:
    print("%s has children %s with weight %s and age %s" % row)