# Check for one and only one command-line argument
if [[ $# != 1 ]]
then
  echo "Usage: ./sensor_sum.sh <filename>"
  exit 1
fi

# File name variable
file=$1

# Check if the file is readable
if [[ ! -r $file ]]
then
  echo "Error: $file is not a readable file!"
  exit 2
fi

# Read in the values from the file
while read sensor x y z
do
  SensorNumber=$(echo $sensor | cut -d'-' -f1)
  echo "$SensorNumber $(($x + $y + $z))"
done < $file

exit 0
