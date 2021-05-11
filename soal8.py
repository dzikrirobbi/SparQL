# Select all people that have niece/nephew

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?child ?sibling WHERE {
        ?subject a ?person .
        FILTER( STRSTARTS(STR(?person),str(g:Father)) ) .
        ?subject g:hasChild ?child .
        ?child g:hasSibling ?sibling .
    }
    """)
for row in qres:
    print("%s has children %s and niece %s" % row)

# Result :
# http://www.owl-ontologies.com/generations.owl#Peter has children http://www.owl-ontologies.com/generations.owl#Matthew and niece http://www.owl-ontologies.com/generations.owl#Gemma