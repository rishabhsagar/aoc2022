# set location vars
cwd_dir=$(pwd)
root_dir="./simulate"

total_size=$(find "${cwd_dir}/${root_dir}" -type f -exec cat {} \; | jq -s add)
free_space=$((70000000 - total_size))
needed_space=$((30000000 - free_space))

echo "Free space ${free_space} out of ${total_size} - Need ${needed_space}"

to_delete=70000000

for dir in $(find "${cwd_dir}/${root_dir}" -type d)
do
    this_dir_size=$(find "$dir" -type f -exec cat {} \; | jq -s add)
    if [[ "$this_dir_size" -ge "$needed_space" ]]
    then
        if [[ "$this_dir_size" -lt "$to_delete" ]]
        then
            to_delete="$this_dir_size"
        fi
    fi
done

echo "Directory to delete size: ${to_delete}"
