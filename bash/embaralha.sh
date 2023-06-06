#!/usr/bin/env bash

N=$1
deck=()
for ((i=1;i<$N+1;i++)); do
  deck+=($i)
done

#output=()
#while (($N>1)); do
#  ((N--))
#  output+=(${deck[0]})
#  output+=(",")
#  deck+=(${deck[1]})
#  deck=("${deck[@]:2}")
#done
#echo "[[${output[*]}],${deck[@]}]"
#
#s=""
#for ((i = 0; i < ${#output[@]}; i++))
#do
#    s+="${output[$i]}"
#done
#echo $s

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

#output=(${deck[@]})
#i=0
#while (($N>1)); do
#  ((N--))
#  output[$i]=${deck[0]}
#  ((i++))
#  deck+=(${deck[1]})
#  deck=("${deck[@]:2}")
#done
#echo "[${output[@]:0:$i}] ${deck[@]}"

#output=()
#drop=true
#i=0
#while (($N>1)); do
#  if [ "$drop" = true ]; then
#    drop=false
#    output+=(${deck[$i]})
#    deck=("${deck[@]:$i}") #NÃO FUNCIONA
#    ((N--))
#    echo "i:$i N:$N deck:${deck[@]}"
#  else
#    drop=true
#  fi
#  ((i++))
#  if ((i==$N)); then
#    ((i-=$N))
#  fi
#done
#echo "[${output[@]}] ${deck[@]}"
