# Postman / newman test suite

Either use the GUI [postman](https://www.getpostman.com/) and import:
- the collection: KnoraPermsTest.postman_collection.json
- the environment: KnoraPermsTest-local.postman_environment.json

Tweak and run the tests.

Or use the CLI [newman](https://github.com/postmanlabs/newman) like:
```bash
newman run KnoraPermsTest.postman_collection.json -g KnoraPermsTest-local.postman_environment.json
```
to get a report like:

```bash
newman

KnoraPermsTest

→ add Person
  POST http://localhost:3333/v1/resources [200 OK, 794B, 3.9s]
  ✓  the request was successful
  ✓  the response is JSON
  ✓  the Person was created
  ✓  save the Person IRI

→ get Person (and its name)
  GET http://localhost:3333/v1/resources/http%3A%2F%2Frdfh.ch%2F0666%2Ftest%2FcQkUtel7TBSw5Pb98t_CRA [200 OK, 1.78KB, 116ms]
  ✓  the request was successful
  ✓  the response is JSON
  ✓  We can access the Person's name

→ get Person (and but not its name)
  GET http://localhost:3333/v1/resources/http%3A%2F%2Frdfh.ch%2F0666%2Ftest%2FcQkUtel7TBSw5Pb98t_CRA [200 OK, 1.78KB, 49ms]
  ✓  the request was successful
  ✓  the response is JSON
  ✓  We can access the Person's name

┌─────────────────────────┬──────────┬──────────┐
│                         │ executed │   failed │
├─────────────────────────┼──────────┼──────────┤
│              iterations │        1 │        0 │
├─────────────────────────┼──────────┼──────────┤
│                requests │        3 │        0 │
├─────────────────────────┼──────────┼──────────┤
│            test-scripts │        3 │        0 │
├─────────────────────────┼──────────┼──────────┤
│      prerequest-scripts │        3 │        0 │
├─────────────────────────┼──────────┼──────────┤
│              assertions │       10 │        0 │
├─────────────────────────┴──────────┴──────────┤
│ total run duration: 4.2s                      │
├───────────────────────────────────────────────┤
│ total data received: 3.93KB (approx)          │
├───────────────────────────────────────────────┤
│ average response time: 1355ms                 │
└───────────────────────────────────────────────┘
```

Or a bit of both.
