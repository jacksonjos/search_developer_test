#!/bin/bash

# copia security.json caso o arquivo ainda não exista. Caso o arquivo já exista
# em /opt/solr/server/solr/ a cópia não é realizada

if [ ! -f /opt/solr/server/solr/security.json ]; then
    cp -u /docker-entrypoint-initdb.d/security.json /opt/solr/server/solr/
fi
