#!/usr/bin/env bash

N=$1
deck=()
for ((i=1;i<$N+1;i++)); do
  deck+=($i)
done
output=""
while (($N>1)); do
  ((N--))
  output+="${deck[0]}"
  if (($N>1)); then
    output+=","
  fi
  deck+=(${deck[1]})
  deck=("${deck[@]:2}")
done
echo "[[$output],${deck[@]}]"
