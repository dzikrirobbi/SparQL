# Select all pairs x-y where x is a father and y is his child. At the same time their weights should be different. Show the results in descending order of an age of the children

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject ?child ?weight ?age WHERE {
        ?subject a ?person .
        FILTER( STRSTARTS(STR(?person),str(g:Father)) ) .
        ?subject g:hasChild ?child .
        ?child g:weight ?weight .
        ?child g:hasAge ?age .
    }
    ORDER BY ASC(?age)
    """)
for row in qres:
    print("%s has children %s with weight %s and age %s" % row)

# Result :
# http://www.owl-ontologies.com/generations.owl#Peter has children http://www.owl-ontologies.com/generations.owl#Matthew with weight 69 and age 23
# http://www.owl-ontologies.com/generations.owl#William has children http://www.owl-ontologies.com/generations.owl#Peter with weight 93 and age 48