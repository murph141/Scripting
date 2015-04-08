#!/bin/bash

if [[ $# != 1 ]]
then
  echo "Usage: analysis.bash <input file>"
  exit 1
fi

file=$1

if [[ ! -r $file ]]
then
  echo "Error: $file is not a readable file."
  exit 2
fi

sum=0
j=0
i=0


while read line
do
  set $line

  shift
  shift

  while [[ $# != 1 ]]
  do
    ((sum=sum+$1))
    ((i=i+1))
    shift
  done

  watt[j]=$1

  ((average[j]=sum/i))
  sum=0
  i=0
  ((j=j+1))

done < $file

j=0
i=1

while read line
do
  set $line

  name[j]="$1 $2"

  shift
  shift

  i=1

  while [[ $# != 1 ]]
  do
    value=$1
    ((value=value*100))
    value2=${average[j]}
    ((value2=value2*90))
    if [[ $value < $value2 ]]
    then
      echo "Run $i for ${name[j]} with score $1 was 90% less than average"
    fi
    ((i=i+1))
    shift
  done

  echo "$name scored an average of ${average[j]}"
  ((j=j+1))
done < $file

j=0
best=0

for item in ${average[*]}
do
  ((val=${average[j]}/${watt[j]}))

  if [[ $val > $best ]]
  then
    best=$val
    the_name=${name[j]}
  fi

  ((j=j+1))
done

echo "The best performance per watt was achieved by $the_name at $best"
