import rdflib
g = rdflib.Graph()
res = list(g.query(open("test.rq")))
if res[0] == [True, False, True, False]:
    print("RDFlib supports E notation for xsd:literal")
else:
    print("RDFlib supports E notation for xsd:literal")
    import sys
    sys.exit(1)
