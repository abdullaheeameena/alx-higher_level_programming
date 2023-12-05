#!/bin/bash
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
curl -sH "X-School-User-Id: 98" "$1"

