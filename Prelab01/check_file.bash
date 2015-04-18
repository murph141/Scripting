# Check for correct number of command-line arguments
if [[ $# != 1 ]]
then
  echo "Usage: ./check_file.bash <filename>"
  exit 1
fi

# Set variable to input value
f=$1

# Check for existance
if [[ -e $f ]]
then
  echo "$f exists"
else
  echo "$f does not exist"
fi

# Check if a directory
if [[ -d $f ]]
then
  echo "$f is a directory"
else
  echo "$f is not a directory"
fi

# Check if an ordinary file
if [[ -f $f ]]
then
  echo "$f is an ordinary file"
else
  echo "$f is not an ordinary file"
fi

# Check if readable
if [[ -r $f ]]
then
  echo "$f is readable"
else
  echo "$f is not readable"
fi

# Check if writable
if [[ -w $f ]]
then
  echo "$f is writable"
else
  echo "$f is not writable"
fi

# Check if executable
if [[ -x $f ]]
then
  echo "$f is executable"
else
  echo "$f is not executable"
fi

exit 0
