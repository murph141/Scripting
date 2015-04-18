# Interate through the command line arguments
for arg in $@
do
  if [[ -r $arg ]]
  then
    # Print if the file exists and is readable
    echo "File $arg is readable!"
  else
    if [[ ! -e $arg ]]
    then
      # Create an empty file if it doesn't exist
      touch $arg
    fi
  fi
done

exit 0
