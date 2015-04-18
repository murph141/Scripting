if [[ $# != 1 ]]
then
  echo "Usage: process_temps.bash <input file>"
  exit 1
fi

file=$1

if [[ ! -r $file ]]
then
  echo "Error: $file is not a readable file."
  exit 2
fi

sum=0
i=0
first_line=1
re='^[0-9]+$'

while read line
do
  set $line

  time=$1

  shift

  while [[ $# != 0 ]]
  do
    ((sum=sum+$1))
    ((i=i+1))
    shift
  done

  if [[ $time =~ $re ]]
  then
    echo "Average temperature for time $time was $((sum / i)) C."
  fi

  sum=0
  i=0
done < $file
