# Test Git
import rdflib

g = rdflib.Graph()
g.parse("family.ttl", format='ttl')

qres = g.query("""
PREFIX g: <http://www.owl-ontologies.com/generations.owl#>
    SELECT ?subject WHERE {
        ?subject a g:Father	
    }
    """)

# print("Name")
# print("_______________________________________________________")
# print(" ")
for row in qres:
    print("%s" % row)
    # print("_______________________________________________________")
    # print(" ")
    