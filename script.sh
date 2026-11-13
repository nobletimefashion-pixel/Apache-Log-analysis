#!/bin/bash

echo "List of top 5 Attacking IP addresses identified"

grep "Failed password" auth.log \
  | awk '{print $(NF-3)}' \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 5 \
  | sed -E 's/^[[:space:]]*([0-9]+)[[:space:]]+(.*)/IP: \2 - Failed Attempts: \1/'