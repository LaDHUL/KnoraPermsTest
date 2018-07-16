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
