#!/bin/bash

echo "List of top 5 Attacking IP addresses identified"

grep "Failed password" auth.log \
  | awk '{print $(NF-3)}' \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 5 \
  | sed -E 's/^[[:space:]]*([0-9]+)[[:space:]]+(.*)/IP: \2 - Failed Attempts: \1/'

TOP_IP=$(grep "Failed password" auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | awk 'NR==1 {print $2}')
grep "Failed password.*$TOP_IP" auth.log | awk -v ip="$TOP_IP" 'NR==1{first=$1" "$2" "$3} {last=$1" "$2" "$3} END{cmd1="date -d \""first"\" +%s"; cmd2="date -d \""last"\" +%s"; cmd1|getline t1; cmd2|getline t2; printf "\nTop IP (%s) Window: First=%s | Last=%s | Span=%.1f mins (%.1f hrs)\n", ip, first, last, (t2-t1)/60, (t2-t1)/3600}'