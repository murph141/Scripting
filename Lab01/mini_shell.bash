#!/bin/bash

while ((1 == 1))
do
  echo -n "Enter a command: "
  read command

  if [[ "$command" == "hello" ]]
  then
    echo "Hello $USER"

  elif [[ "$command" == "quit" ]]
  then
    echo "Exiting..."
    exit 0

  elif [[ "$command" == "compile" ]]
  then

    echo -n "Enter filename: "
    read file

    if [[ -r $file ]]
    then
      $(gcc -Wall -Werror $file)

      if [[ $? == 0 ]]
      then
        echo "Compilation succeeded"
      else
        echo "Compilation failed"
      fi

    else
      echo "That file does not exist"
    fi

  else
    echo "Error: Unrecognized input"
  fi

done
