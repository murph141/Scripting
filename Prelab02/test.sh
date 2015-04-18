A[27]="x"
A[6]="y"
A[86]="z"

echo "${!A[*]}"

for I in ${A[*]}
do
  echo "$I"
done

USER_ID=$(basename $(cd ../ && pwd))

echo "$USER_ID"
