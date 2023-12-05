#!/bin/bash
[ -z "$2" ] && echo "Usage: $0 <URL> <JSON file>" && exit 1
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

