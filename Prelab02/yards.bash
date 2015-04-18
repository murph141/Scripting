if [[ $# < 1 ]]
then
  echo "Usage: yards.bash <filename>"
  exit 1
fi

file=$1

if [[ ! -r $file ]]
then
  echo "Error: $file is not readable"
  exit 2
fi

sum=0
num=0
i=0
high_average=0

while read line
do
  set $line

  shift

  while [[ $# != 0 ]]
  do
    ((sum=sum+$1))
    ((num=num+1))
    shift
  done

  ((average[i]=sum/num))

  if [[ ${average[i]} > $high_average ]]
  then
    high_average=${average[i]}
  fi

  ((i=i+1))
  num=0
  sum=0

done < $file

stddev=0
num=0
i=0

while read line
do
  set $line

  echo -n "$1 schools averaged "

  shift

  while [[ $# != 0 ]]
  do
    ((stddev=stddev+(($1 - ${average[i]})) * (($1 - ${average[i]}))))
    ((num=num+1))
    shift
  done

  ((stddev=stddev/num))

  echo "${average[i]} yards receiving with a variance of $stddev"

  num=0
  stddev=0
  ((i=i+1))

done < $file

echo "The largest average yardage was $high_average"
