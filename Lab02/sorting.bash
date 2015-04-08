#!/bin/bash

if [[ $# != 1 ]]
then
  echo "Usage: ./sorting.bash <input file>"
  exit 1
fi

file=$1

if [[ ! -r $file ]]
then
  echo "Error: $file is not a readable file."
  exit 2
fi

choice=0

echo "Your choices are:"
echo '1) First 10 people'
echo '2) Last 5 names by highest zipcode'
echo '3) Address of 6th-10th by reverse e-mail'
echo '4) First 12 companies'
echo '5) Pick a number of people'
echo '6) Exit'

while [[ 1 ]]
do
  echo -n 'Your choice: '

  read choice

  if [[ $choice == 1 ]]
  then
    sort -f -t ',' -k7,7 -k5,5 -k2,2 -k1,1 $file | head
  elif [[ $choice == 2 ]]
  then
    sort -n -r -t ',' -k8,9 $file | head -n 5 | sort -n -t ',' -k8,9 | cut -d',' -f2,1
  elif [[ $choice == 3 ]]
  then
    sort -r -t ',' -k11 $file | cut -d ',' -f4 | head | tail -n 5
  elif [[ $choice == 4 ]]
  then
    sort -f -t ',' -k3 $file | cut -d',' -f3 | head -n 12
  elif [[ $choice == 5 ]]
  then
    echo -n "Enter a number: "
    read num
    sort -f -t ',' -k2 -k1 $file | head -n$num
  elif [[ $choice == 6 ]]
  then
    echo "Have a nice day!"
    exit 0
  else
    echo "Error! Invalid Selection!"
  fi
done

# Your expected output it wrong on your labs
