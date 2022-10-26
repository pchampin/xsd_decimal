# `xsd:decimal` and the E notation

This repository aims at

* discussing a possible future evolution of `xsd:decimal` to support [E notation], and
* keep track of the current state of implementations.

## The problem

The `xsd:decimal` datatype is [defined in a way] that it only support the "simple" decimal notation (e.g. `12.3`) but not the [E notation] (e.g. `1.23E1`).

This can be a problem when `xsd:decimal` values are generated programmatically. In particular, in JSON-LD, [type coercion used with JSON numbers] can lead to decimals expressed with the [E notation], which are  ill-formed, according to the standard.

## The ideal solution

It is not entirely clear why the [E notation] is was allowed for `xsd:decimal`.
If a new version of [XSD Datatypes] is published, it would seem like a good idea in extend `xsd:decimal` to support [E notation].

## In the meantime (a pragmatic solution)

As a matter of fact, many RDF and related implementations already support the [E notation] for `xsd:decimal` (see below).
So in practice, it might be relatively safe to use it, even though it is not (yet?) standard.

### Implementations that support `xsd:decimal` with [E notation]

| Implementation | Version | Evidence |
| -------------- | ------- | -------- |
| [GraphDB](https://graphdb.ontotext.com/) | 10.0.2 | tested with [test.rq](test.rq) |
| [Virtuoso](https://virtuoso.openlinksw.com/) | 8.03 | tested with [test.rq](test.rq), [try online](https://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&qtxt=PREFIX%20xsd%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0ASELECT%20%0A%20%20(%2201.10%22%5E%5Exsd%3Adecimal%20%3D%20%221.1%22%5E%5Exsd%3Adecimal%20as%20%3Fstd_true)%0A%20%20(%2201.10%22%5E%5Exsd%3Adecimal%20%3D%20%221.2%22%5E%5Exsd%3Adecimal%20as%20%3Fstd_false)%0A%20%20(%2201.10%22%5E%5Exsd%3Adecimal%20%3D%20%2211e-1%22%5E%5Exsd%3Adecimal%20as%20%3Fexp_true)%0A%20%20(%2201.10%22%5E%5Exsd%3Adecimal%20%3D%20%2211e-2%22%5E%5Exsd%3Adecimal%20as%20%3Fexp_false)%0A%7B%7D%0A%0A%23%20If%20the%20result%20of%20this%20query%20is%20true%2C%20false%2C%20true%2C%20false%0A%23%20then%20this%20SPARQL%20implementation%20correctly%20supports%20the%20E%20notation%20for%20xsd%3Adecimal%0A&format=text%2Fhtml&timeout=30000&signal_void=on&signal_unconnected=on) |
| [Qlever](https://github.com/ad-freiburg/qlever) | [latest on 22-10-24](https://hub.docker.com/r/adfreiburg/qlever/tags) | tested with [test_qlever.rq](test_qlever.rq) |
| [RDFlib](https://rdflib.dev/) | 6.2.0 | tested with [test_rdflib.py](test_rdflib.py) |
| [Hermit](http://www.hermit-reasoner.com/) | 1.3.8 | tested with [test.owl.ttl](test.owl.ttl) |
| [Eye](https://github.com/josd/eye/) | v22.1021.1922 | tested with [test.n3](test.n3), [try online](http://ppr.cs.dal.ca:3002/n3/editor/s/OCzy4xYF) |
| [CWM](https://linkeddata.github.io/swap/doc/cwm.html) | 1.197 | tested with [test.n3](test.n3), [try online](http://ppr.cs.dal.ca:3002/n3/editor/s/OCzy4xYF) |

### Implementations that support `xsd:decimal` WITHOUT [E notation]


| Implementation | Version | Evidence |
| -------------- | ------- | -------- |
| [Apache Jena](https://jena.apache.org/) | 10.0.2 | tested with [test.rq](test.rq) |
| [Corese](https://project.inria.fr/corese/) | [commit 3ebe016](https://github.com/Wimmics/corese/commit/3ebe01681b28ec32a4b6e92fda494572c3af88b8) | tested with [test.rq](test.rq) |
| [Oxigraph](https://github.com/oxigraph/oxigraph) | [commit 825b330](https://github.com/oxigraph/oxigraph/commit/825b330132ebfc0f1669b4c2ec2529a96a9a11dd) | tested with [test.rq](test.rq) |
| [Ruby RDF](https://ruby-rdf.github.io/) | 3.2.9 | tested with [test.rq](test.rq) |


### Contributing

If you know of another implementation that does not appear in the tables above,
or of any change with a new version of one that does appear,
please make a pull-request adding or updating a line in the appropriate table,
following the model of other lines.

[defined in a way]: https://www.w3.org/TR/xmlschema11-2/#decimal
[E notation]: https://en.wikipedia.org/wiki/Scientific_notation#E_notation
[type coercion used with JSON numbers]: https://json-ld.org/playground/#startTab=tab-nquads&json-ld=%7B%22%40context%22%3A%7B%22ex%22%3A%22http%3A%2F%2Fexample.com%2Fns%2F%22%2C%22xsd%22%3A%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%22%2C%22ex%3Afoo%22%3A%7B%22%40type%22%3A%22xsd%3Adecimal%22%7D%7D%2C%22ex%3Afoo%22%3A%5B12.3%5D%7D 
[XSD Datatypes]: https://www.w3.org/TR/xmlschema11-2/
