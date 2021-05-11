# Select all Men, and optionally their children and their parents if this information is available

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

# Result :
# http://www.owl-ontologies.com/generations.owl#Matthew has children None and parent http://www.owl-ontologies.com/generations.owl#Peter
# http://www.owl-ontologies.com/generations.owl#Peter has children http://www.owl-ontologies.com/generations.owl#Matthew and parent http://www.owl-ontologies.com/generations.owl#William
# http://www.owl-ontologies.com/generations.owl#William has children http://www.owl-ontologies.com/generations.owl#Peter and parent None