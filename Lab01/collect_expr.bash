#!/bin/bash

output_file=$1
number=$(($# - 1))

if [[ $# < 2 ]]
then
  echo "usage: collect_expr.bash <output file> <input file 1> [input file 2] ... [input file N]"
  exit 1
fi

if [[ -e $output_file ]]
then
  echo "error: output file $output_file already exists!"
  exit 2
fi

i=0

for arg in $@
do
  if [[ $i == 0 ]]
  then
    i=1
    continue
  fi

  if [[ ! -r $arg ]]
  then
    echo "error: input file $arg is not readable!"
    exit 2
  fi
done

for arg in $@
do
  if [[ $i == 1 ]]
  then
    i=2
    continue
  fi

  while read user d1 d2 d3 d4 d5
  do
    sum=$(($d1 + $d2 + $d3 + $d4 + $d5))
    echo "$user $d1 $d2 $d3 $d4 $d5 $sum $(($sum / 5))" >> $1
  done < $arg
done
