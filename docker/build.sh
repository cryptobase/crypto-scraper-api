#!/bin/sh

mkdir -p app
cp ../*.py app
cp -r ../templates app

docker build -t cryptobase/scraper-api .
