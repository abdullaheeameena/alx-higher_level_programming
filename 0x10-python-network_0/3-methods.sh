#!/bin/bash
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print $2}'

