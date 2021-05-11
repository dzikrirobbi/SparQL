# Select all parents older than 30 who do not have any information whether he/she has parent

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

# Result :
# http://www.owl-ontologies.com/generations.owl#William