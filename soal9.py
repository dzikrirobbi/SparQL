# Select all persons who belong to the class OffSpring

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject WHERE {
        ?subject a g:OffSpring	
    }
    """)

for row in qres:
    print("%s" % row)
    
# Result : 
# http://www.owl-ontologies.com/generations.owl#Matthew
# http://www.owl-ontologies.com/generations.owl#Peter