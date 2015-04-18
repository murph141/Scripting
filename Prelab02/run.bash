if [[ $# != 2 ]]
then
  echo "Usage: ./run.bash <source_file> <output_file>"
  exit 1
fi

if [[ -e quick_sim ]]
then
  rm -rf quick_sim
fi

output=$2

if [[ -e $output ]]
then
  echo -n "$output exists. Would you like to delete it? "
  read answer

  if [[ $answer == 'y' || $answer == 'yes' ]]
  then
    new=''
    while [[ $new == '' ]]
    do
      echo -n "Enter a new filename: "
      read new
    done
    output=$new
  else
    rm $output
  fi
fi

gcc $1 -o quick_sim

if [[ $? != 0 ]]
then
  echo "error: quick_sim could not be compiled!"
  exit 1
fi

cache=(1 2 4 8 16 32)
issue=(1 2 4 8 16)
processor=('a' 'i')

echo -n "" > $output

for i in ${cache[*]}
do
  for j in ${issue[*]}
    do
      for k in ${processor[*]}
      do
        quick_sim $i $j $k | sed 's_.*\(:.*:\).*\(:.*:\).*\(:.*:\).*\(:.*:\).*\(:.*\)_\1 \2 \3 \4 \5_' | sed 's_:__' | sed 's_:\ :_:_g' >> $output
      done
    done
done

fastest=$(cut -d':' -f5 $output | sort -n | head -n 1)
Arr=$(grep $fastest $output | sed 's_:_ _g')

set $Arr

echo "Fastest run time achieved by $1 $2 $3 with cache size $4 and issue width $5 was $7"
