# Return an amount of people that have parent

import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT (count(distinct ?subject) as ?count) WHERE {
        ?subject g:hasParent ?person .
    }
    """)

for row in qres:
    print("Counting : %s people's" % row)

# Result :
# Counting : 2 people's