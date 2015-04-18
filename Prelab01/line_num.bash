# Check for one and only one command-line argument
if [[ $# != 1 ]]
then
  echo "Usage: line_num.bash <filename>"
  exit 1
fi

# Set a file variabl
file=$1

# Check if the file can be read
if [[ ! -r $file ]]
then
  echo "Cannot read $file"
  exit 1
fi

# Counter variable
i=1

# Read the file line by line
while read line
do
  echo "$i:$line"
  ((i=i+1))
done < $1

exit 0
