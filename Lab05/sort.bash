#!/bin/bash

file='a'
column='a'

while getopts f:-: thisopt
do
  case $thisopt in
    f)file=$OPTARG;;
    -)val=$(echo $OPTARG | cut -d'=' -f2)
      column=$val;;
    *)echo "Error: Unknown option."
      exit 1;;
  esac
done 2>/dev/null 

if [[ ! -e $file ]]
then
  echo "Error: File does not exist."
  exit 1
fi

if [[ ! -r $file ]]
then
  echo "Error: File is not readable."
  exit 1
fi

if [[ $file == 'a' || $column == 'a' ]]
then
  echo "Error: Insufficient information."
  exit 1
fi

i=0
while read line
do
  set $line
  i=0

  while [[ $# != 1 ]]
  do
    ((i=i+1))
    shift
  done
done < $file

if [[ $column > $i ]]
then
  echo "Error: Column number $column does not exist."
  exit 1
fi

((column=column+1))

sort -n -k$column $file > $file.sorted

echo "File sorted."

exit 0
