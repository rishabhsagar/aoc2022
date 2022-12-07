# set location vars
cwd_dir=$(pwd)
root_dir="./simulate"

# create needed dirs
rm -rf "$root_dir"
mkdir "$root_dir"
cd "$root_dir"
# ls contents
ls_output=0

while read -r term_input
do
  if [[ "$ls_output" -eq 1 ]]
  then
    if [[ ! "$term_input" =~ ^\$.*$ ]]
    then
      if [[ "$term_input" =~ ^dir.*$ ]]
      then
        mkdir "${term_input/* /}"
      else
        echo "${term_input/ */}" > "${term_input/* /}"
      fi
    else
      ls_output=0
    fi
  fi

  if [[ "$ls_output" -eq 0 ]]
  then
    if [[ "$term_input" =~ ^\$.*cd.*$ ]]
    then
      cd ./"${term_input/* /}"
    elif [[ "$term_input" =~ ^\$.*ls$ ]]
    then
      ls_output=1
    fi
  fi
done < ../data/input.txt

total=0
for directory in $(find "${cwd_dir}/${root_dir}" -type d)
do
  dir_size=$(find "$directory" -type f -exec cat {} \; | jq -s add)
  if [[ "$dir_size" -le 100000 ]]
  then
    total=$((total + dir_size))
  fi
done

echo "Total directories above 100K: $total"
