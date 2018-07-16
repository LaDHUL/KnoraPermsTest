# attention : bulk import seulement avec un user admin

```
$ iri=$(curl -s -u test-proj-admin-user@unil.ch:test -X POST -d @person1.xml http://localhost:3333/v1/resources/xmlimport/http%3A%2F%2Frdfh.ch%2Fprojects%2F0666 | jq '.createdResources[0].resourceIri'|tr -d '"')
```

# import avec un user non admin

```
$ iri=$(curl -s -u test-proj-basic-user@unil.ch:test -X POST -H "Content-Type: application/json" -d @person1.json http://localhost:3333/v1/resources |jq '.res_id'|tr -d '"')
$ echo $iri
```
