file=file_list
i=0

# Create an array of values
while read line
do
  a[i]=$line
  ((i=i+1))
done < $file

# Iterate through the array
for line in ${a[*]}
do
  updated=$(svn status $line | cut -c 1)

  if [[ ! -e $line ]]
  then
    if [[ -z $updated ]]
    then
      echo "Error: File $line appears to not exist here or in svn"
      exit 1
    fi
  else

    if [[ $updated  == '?' ]]
    then
      if [[ ! -x $line ]]
      then 

        echo "Do you want to make the file ($line) executable? "
        read response

        if [[ $response == 'y' ]]
        then
          chmod +x $line
        fi
      fi

      svn add $line
    else
      if [[ ! -x $line ]]
      then
        svn propset svn:executable ON $line
      fi
    fi
  fi
done

svn commit -m 'Auto-committing code'

exit 0
