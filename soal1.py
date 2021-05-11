# Select all persons who belong to the class Father

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject WHERE {
        ?subject a g:Father	
    }
    """)

for row in qres:
    print("%s" % row)
    
# Result : 
# http://www.owl-ontologies.com/generations.owl#Peter
# http://www.owl-ontologies.com/generations.owl#William