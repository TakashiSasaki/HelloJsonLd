import rdflib
n3  = '''
@prefix dc: <http://purl.org/dc/terms/> .
<http://example.org/about> dc:title "Someone's Homepage"@en .
<#pat> <#knows> <#jo> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix : <#> .
:pat :child [ :age 4 ] , [ :age 3 ].
:Person a rdfs:Class.
:Person rdf:type rdfs:Class.
:Pat a :Person.
:Woman a rdfs:Class; rdfs:subClassOf :Person .
:sister a rdf:Property.
:sister rdfs:domain :Person; 
        rdfs:range :Woman.
:Woman = :FemaleAdult .
:Title a rdf:Property; = dc:title .
'''

g = rdflib.Graph().parse(data=n3, format="n3")
print(g.serialize(format="json-ld", indent=4).decode('utf8'))

