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