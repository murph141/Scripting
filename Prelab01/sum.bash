# Sum starts at 0
sum=0

# While command line arguments exist
while (( $# != 0 ))
do
  # Sum is incremented by the command line value
  ((sum=sum+$1))

  # The command line argument is shifted out
  shift
done

# Print the sum
echo $sum

exit 0
