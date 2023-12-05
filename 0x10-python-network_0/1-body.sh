#!/bin/bash
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
curl -sL -w "%{http_code}" "$1" | awk 'NR>1 {print} /^200$/'

