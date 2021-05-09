import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject WHERE {
        ?subject g:hasAge ?age .
        FILTER NOT EXISTS { ?subject g:hasParent ?parent }
        FILTER( ?age > 30) 
    }
    """)
    
for row in qres:
    print("%s" % row)