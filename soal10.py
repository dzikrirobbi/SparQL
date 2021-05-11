# Select all persons who belong has sibling

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?sibling WHERE {
        ?subject g:hasSibling ?sibling .
    }
    """)

for row in qres:
    print("%s has sibling %s" % row)
    
# Result : 
# http://www.owl-ontologies.com/generations.owl#Matthew has sibling http://www.owl-ontologies.com/generations.owl#Gemma
# http://www.owl-ontologies.com/generations.owl#Gemma has sibling http://www.owl-ontologies.com/generations.owl#Matthew