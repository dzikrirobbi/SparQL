# Select all persons who belong to either of Brother or Sister class

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject WHERE {
        ?subject a ?person .
        FILTER( STRSTARTS(STR(?person),str(g:Sister)) || STRSTARTS(STR(?person),str(g:Brother))) .
    }
    """)
    
for row in qres:
    print("%s" % row)

# Result :
# http://www.owl-ontologies.com/generations.owl#Gemma
# http://www.owl-ontologies.com/generations.owl#Matthew