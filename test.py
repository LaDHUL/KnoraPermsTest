#!/usr/bin/env python3

import datetime
import json
import sys
import time

import requests

KNORA_BASE_URL = "http://0.0.0.0:3333"
ADMIN_USER = "root@example.com"
ADMIN_PWD = "test"

PROJ_SHORTCODE = "FFFE"


def checkErrorAndExit(r):
    if not r.ok:
        print("*** ERROR ***")
        print(r)
        print(r.status_code)
        print(r.text)
        sys.exit(1)


def initTestProject():
    r = requests.get(KNORA_BASE_URL+'/admin/projects/' +
                     PROJ_SHORTCODE + '?identifier=shortcode')
    # project already existing
    if(r.status_code == 404):
        r = requests.post(
            KNORA_BASE_URL+'/admin/projects',
            json={
                "shortcode": PROJ_SHORTCODE,
                "shortname": PROJ_SHORTCODE+"Test",
                "description": [PROJ_SHORTCODE+" test project"],
                "keywords": [PROJ_SHORTCODE+" keywords"],
                "status": True,
                "selfjoin": False
            },
            auth=(ADMIN_USER, ADMIN_PWD))
        checkErrorAndExit(r)
        print(" - Test project not found and recreated")
    return json.loads(r.text)


def createOntology(project_json, name):
    r = requests.post(
        KNORA_BASE_URL+'/v2/ontologies',
        json={
            "knora-api:ontologyName": name,
            "knora-api:attachedToProject": {
                "@id": project_json['project']['id']
            },
            "rdfs:label": name,
            "@context": {
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "knora-api": "http://api.knora.org/ontology/knora-api/v2#"
            }},
        auth=(ADMIN_USER, ADMIN_PWD)
    )
    checkErrorAndExit(r)
    print(" - Ontology %s created" % name)
    return json.loads(r.text)


def createClass(onto_json, name):
    r = requests.post(
        KNORA_BASE_URL+'/v2/ontologies/classes',
        json={
            "@id": onto_json["@id"],
            "@type": "owl:Ontology",
            "knora-api:lastModificationDate": onto_json["knora-api:lastModificationDate"],
            "@graph": [{
                       "@id": "onto:"+name,
                       "@type": "owl:Class",
                       "rdfs:label": {
                           "@language": "en",
                           "@value": name
                       },
                       "rdfs:comment": {
                           "@language": "en",
                           "@value": name + " comment"
                       },
                       "rdfs:subClassOf": {
                           "@id": "knora-api:Resource"
                       }
                       }],
            "@context": {
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                       "knora-api": "http://api.knora.org/ontology/knora-api/v2#",
                       "owl": "http://www.w3.org/2002/07/owl#",
                       "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                       "xsd": "http://www.w3.org/2001/XMLSchema#",
                       "onto": onto_json["@id"]+"#"
            }
        },
        auth=(ADMIN_USER, ADMIN_PWD)
    )
    checkErrorAndExit(r)
    print(" - Ontology %s created" % name)
    return json.loads(r.text)


start = time.time()
print("")

project_json = initTestProject()
print(" - Test project:\n%s" % json.dumps(project_json, indent=2))
print("")

onto_json = createOntology(
    project_json, "TestOnto_"+time.strftime("%d.%m.%Y_%H-%M-%S"))
print(" - Test onto:\n%s" % json.dumps(onto_json, indent=2))

class_json = createClass(onto_json, "TestClass")
print(" - Test class:\n%s" % json.dumps(class_json, indent=2))

print(" - Done [%s s]" %
      (str(time.time() - start)))
print("")
