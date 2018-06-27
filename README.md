```
$ wget http://localhost:3333/v1/resources/xmlimportschemas/http%3A%2F%2Fwww.knora.org%2Fontology%2F0666%2Ftest -O schema.zip

$ unzip schema.zip
Archive: schema.zip
inflating: p0666-test.xsd
inflating: knoraXmlImport.xsd
```

# attention : bulk import seulement avec un user admin

```
$ iri=$(curl -s -u test-proj-admin-user@unil.ch:test -X POST -d @person1.xml http://localhost:3333/v1/resources/xmlimport/http%3A%2F%2Frdfh.ch%2Fprojects%2F0666 | jq '.createdResources[0].resourceIri'|tr -d '"')
```

# import avec un user non admin

```
$ iri=$(curl -s -u test-proj-basic-user@unil.ch:test -X POST -H "Content-Type: application/json" -d @person1.json http://localhost:3333/v1/resources |jq '.res_id'|tr -d '"')
$ echo $iri
```

# encode url func

```
$ alias urlencode='python2 -c "import sys, urllib as ul; print ul.quote_plus(sys.argv[1])"'
```

# test:hasName non présent pour UnknownUser

```
$ curl -X GET http://localhost:3333/v2/resources/$(urlencode $iri)
```

# test:hasName présent pour un user connecté

```
$ curl -u test-proj-basic-user@unil.ch:test -X GET http://localhost:3333/v2/resources/$(urlencode $iri)
```

# fonctionne aussi avec draftperson1.json : perms utilise l'héritage
