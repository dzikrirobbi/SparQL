# Select all persons who belong has uncle/aunt

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?parent WHERE {
        ?subject g:hasSibling ?sibling .
        ?sibling g:hasParent ?parent .
    }
    """)
for row in qres:
    print("%s has uncle/aunt %s" % row)
    
# Result : 
# http://www.owl-ontologies.com/generations.owl#Gemma has uncle/aunt http://www.owl-ontologies.com/generations.owl#Peter