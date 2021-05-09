import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?child ?parent WHERE {
        ?subject a ?person .
        FILTER( STRSTARTS(STR(?person),str(g:Male)) ) .
        OPTIONAL { ?subject g:hasChild ?child } .
        OPTIONAL { ?subject g:hasParent ?parent }
    }
    """)
    
for row in qres:
    print("%s has children %s and parent %s" % row)