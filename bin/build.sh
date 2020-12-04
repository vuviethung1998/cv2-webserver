#!/usr/bin/env bash9
docker build -t c_search .
docker tag c_search:latest cendev3:5005/c_search:d.1.17.1
docker push cendev3:5005/c_search:d.1.17.1


docker build -t c_search .
docker tag c_search:latest webapp:5005/c_search:p.1.14.61
docker push webapp:5005/c_search:p.1.14.61